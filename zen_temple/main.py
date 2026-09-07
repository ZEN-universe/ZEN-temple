import socket
import webbrowser
from argparse import ArgumentParser, BooleanOptionalAction
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import config
from .routers import solution_router

# Initialize default app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize api app
api_app = FastAPI()
api_app.include_router(solution_router.router)
app.mount("/api", api_app)

_PLACEHOLDER_INDEX = """<!doctype html>
<html lang="en">
<head>
\t<meta charset="utf-8">
\t<meta name="viewport" content="width=device-width, initial-scale=1">
\t<title>ZEN temple</title>
</head>
<body>
\t<h1>Welcome to ZEN temple</h1>
\t<p>The ZEN-explorer frontend has not been fetched yet. Run <code>zen-temple-fetch-explorer</code> to download it, or build ZEN-explorer from source and copy it into the <code>zen_temple/explorer/</code> folder.</p>
</body>
</html>
"""


def _ensure_explorer_dir(path: Path) -> None:
    """Make sure the explorer directory exists so StaticFiles can mount it.

    The directory contents are gitignored and only populated by the release
    build or by ``zen-temple-fetch-explorer``. On a fresh editable checkout it
    can be missing entirely, so seed it with a placeholder page.
    """
    path.mkdir(parents=True, exist_ok=True)
    index = path / "index.html"
    if not index.exists():
        index.write_text(_PLACEHOLDER_INDEX, encoding="utf-8")


def _check_explorer_populated(path: Path) -> None:
    """Fail early with a helpful message if the ZEN-explorer build is missing.

    In an editable install the ``explorer`` folder only holds the placeholder
    page until the frontend is fetched, so ``_app/`` (the SvelteKit build) does
    not exist yet and the server would crash while writing ``_app/env.js``.
    """
    if (path / "_app").is_dir():
        return
    raise SystemExit(
        "The ZEN-explorer frontend has not been fetched yet, so the "
        "visualization platform cannot start.\n"
        f"Expected build files in: {path}\n\n"
        "Run\n"
        "    zen-temple-fetch-explorer\n"
        "to download them from the latest published release (add "
        "'--version <x.y.z>' to pin one), or build ZEN-explorer from source "
        "and copy its 'build/' contents into that folder."
    )


# Mount explorer as static files
explorer_path = Path(__file__).parent / "explorer"
_ensure_explorer_dir(explorer_path)
explorer_url = "/"
app.mount(explorer_url, StaticFiles(directory=explorer_path, html=True), name="explorer")


def _check_port_available(host: str, port: int) -> None:
    """Fail early with a clear message if the server port is already taken.

    """
    try:
        addr_infos = socket.getaddrinfo(host, port, type=socket.SOCK_STREAM)
    except socket.gaierror:
        # Let uvicorn deal with a host name it cannot resolve.
        return

    for family, socktype, proto, _canonname, sockaddr in addr_infos:
        with socket.socket(family, socktype, proto) as probe:
            if family == socket.AF_INET6 and hasattr(socket, "IPV6_V6ONLY"):
                probe.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
            try:
                probe.bind(sockaddr)
            except OSError as exc:
                raise SystemExit(
                    f"Cannot start the ZEN-temple server: port {port} on "
                    f"'{host}' is not available ({exc}).\n"
                    "Another 'zen-visualization' instance is most likely still "
                    "running on this port."
                ) from exc


def start_server(
    solution_folder: str,
    port: int,
    app_name: str | None = None,
    debug: bool | None = None,
    api_url: str | None = None,
    significant_digits: int | None = None,
    reload: bool = False,
    no_open_browser: bool = False,
    fd: int | None = None,
    api_only: bool = False,
) -> None:
    if api_url is None:
        api_url = f"http://127.0.0.1:{port}/api/"
    if app_name is None:
        app_name = ""

    config.SOLUTION_FOLDER = solution_folder
    if debug is not None:
        config.APP_DEBUG = debug
    if significant_digits is not None:
        config.RESPONSE_SIGNIFICANT_DIGITS = significant_digits

    # When binding by file descriptor uvicorn does not open the port itself.
    if fd is None:
        _check_port_available("localhost", port)

    if api_only:
        # Frontend developers run the ZEN-explorer dev server separately, so the
        # bundled frontend is neither needed nor served here.
        print(f"Serving the ZEN-temple API only at http://localhost:{port}/api/")
    else:
        _check_explorer_populated(explorer_path)
        env_file = explorer_path / "_app" / "env.js"
        with open(env_file, "w") as file:
            file.write(
                f'export const env={{"PUBLIC_TEMPLE_URL":"{api_url}", "PUBLIC_APP_NAME":"{app_name}"}}'
            )
        if not no_open_browser:
            webbrowser.open(f"http://localhost:{port}/explorer/", new=2)
        print(f"Open Visualization platform at http://localhost:{port}/explorer/")
    uvicorn.run(
        "zen_temple.main:app",
        host="localhost",
        port=port,
        log_level="info",
        reload=reload,
        fd=fd,
    )


def find_outputs_folder(outputs_folder: str | None) -> str:
    """
    Verify if the outputs folder exists. Otherwise, goes through a list of default paths.
    If none of the default paths exist, it raises an error.
    """
    if outputs_folder is not None:
        outputs_path = Path(outputs_folder)
    else:
        outputs_path = Path.cwd() / "outputs"
        if not outputs_path.exists():
            outputs_path = Path.cwd()

    # Check if the outputs folder contains a scenarios.json file, i.e. that it is a valid outputs folder
    scenario_files = outputs_path.glob("**/scenarios.json")
    if not any(scenario_files):
        raise FileNotFoundError(
            f"No scenarios.json files found in the outputs folder: {outputs_path}. "
            "Please provide a valid outputs folder using '-o <path-to-folder>'."
        )
    return str(outputs_path)


def parse_arguments_and_run() -> None:
    parser = ArgumentParser(
        description="ZEN Temple - Visualization web platform for ZEN Garden"
    )

    group = parser.add_argument_group("Server Options")
    group.add_argument(
        "-p",
        "--port",
        required=False,
        type=int,
        default=8000,
        help="port on which to run the local server",
    )
    group.add_argument(
        "-o",
        "--outputs-folder",
        "--output",
        required=False,
        type=str,
        default=None,
        help="path to your solutions folder. Per default looks for data in ./outputs or in the current working directory",
    )
    group.add_argument(
        "--significant-digits",
        required=False,
        type=int,
        default=None,
        help="number of significant digits to use in the response. If not set, uses the value from the environment variable RESPONSE_SIGNIFICANT_DIGITS (default: 4)",
    )

    group = parser.add_argument_group("Developer Options")
    group.add_argument(
        "--app-name",
        required=False,
        type=str,
        default="",
        help="name of the app",
    )
    group.add_argument(
        "--debug",
        required=False,
        default=None,
        action=BooleanOptionalAction,
        help="enable/disable debug mode",
    )
    group.add_argument(
        "--api-url",
        required=False,
        type=str,
        default=None,
        help="URL to the API to fetch the data from",
    )
    group.add_argument(
        "--reload",
        required=False,
        action="store_true",
        help="enable reload for development purposes",
    )
    group.add_argument(
        "--no-open-browser",
        required=False,
        action="store_true",
        help="do not open the browser automatically",
    )
    group.add_argument(
        "--api-only",
        required=False,
        action="store_true",
        help=(
            "serve only the REST API and do not require the bundled ZEN-explorer "
            "frontend. Use this when developing ZEN-explorer with its own dev server"
        ),
    )
    group.add_argument(
        "--fd",
        required=False,
        type=int,
        default=None,
        help="file descriptor for the server that the server can bind to",
    )
    args = parser.parse_args()

    outputs_folder = find_outputs_folder(args.outputs_folder)

    start_server(
        outputs_folder,
        args.port,
        app_name=args.app_name,
        debug=args.debug,
        api_url=args.api_url,
        significant_digits=args.significant_digits,
        reload=args.reload,
        no_open_browser=args.no_open_browser,
        fd=args.fd,
        api_only=args.api_only,
    )


if __name__ == "__main__":
    parse_arguments_and_run()
