import os
import webbrowser
from pathlib import Path
from argparse import ArgumentParser

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routers import solutions
from .config import config

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
api_app.include_router(solutions.router)
app.mount("/api", api_app)

# Mount explorer as static files
explorer_path = os.path.join(os.path.dirname(__file__), "explorer")
explorer_url = "/"
app.mount(
    explorer_url, StaticFiles(directory=explorer_path, html=True), name="explorer"
)


def start_server(
    solution_folder: str,
    port: int,
    app_name: str | None = None,
    api_url: str | None = None,
    significant_digits: int | None = None,
    reload: bool = False,
    no_open_browser: bool = False,
    fd: int | None = None,
) -> None:
    if api_url is None:
        api_url = f"http://127.0.0.1:{port}/api/"
    if app_name is None:
        app_name = ""

    config.SOLUTION_FOLDER = solution_folder
    if significant_digits is not None:
        config.RESPONSE_SIGNIFICANT_DIGITS = significant_digits

    env_file = Path(__file__).parent / "explorer" / "_app" / "env.js"
    with open(env_file, "w") as file:
        file.write(
            f'export const env={{"PUBLIC_TEMPLE_URL":"{api_url}", "PUBLIC_APP_NAME":"{app_name}"}}'
        )

    # Start the uvicorn server
    if not no_open_browser:
        webbrowser.open(f"http://localhost:{port}/", new=2)
    uvicorn.run("zen_temple.main:app", host="localhost", port=port, log_level="info", reload=reload, fd=fd)


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
        api_url=args.api_url,
        significant_digits=args.significant_digits,
        reload=args.reload,
        no_open_browser=args.no_open_browser,
        fd=args.fd,
    )


if __name__ == "__main__":
    parse_arguments_and_run()
