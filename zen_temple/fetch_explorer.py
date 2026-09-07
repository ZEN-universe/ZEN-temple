"""Populate ``zen_temple/explorer/`` for editable installs.

The ZEN-explorer frontend is bundled into the wheel during the PyPI release
build (see ``.github/workflows/publish-to-pypi.yml``).  An editable install
(``pip install -e .``) only ships the placeholder page, so the visualization
platform has no UI until the real files are fetched.

This script downloads a published ``zen-temple`` wheel from PyPI and copies its
``zen_temple/explorer/`` payload into the local package directory.  It only uses
the standard library, so no Node.js/npm toolchain is required.
"""

from __future__ import annotations

import argparse
import io
import json
import shutil
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

PYPI_JSON = "https://pypi.org/pypi/zen-temple/json"
PYPI_JSON_VERSION = "https://pypi.org/pypi/zen-temple/{version}/json"
EXPLORER_DIR = Path(__file__).resolve().parent / "explorer"
WHEEL_PREFIX = "zen_temple/explorer/"


def _resolve_wheel_url(version: str | None) -> tuple[str, str]:
    """Return the wheel download URL and the resolved version from PyPI."""
    url = PYPI_JSON_VERSION.format(version=version) if version else PYPI_JSON
    with urllib.request.urlopen(url) as response:  # noqa: S310 - fixed https host
        data: dict[str, Any] = json.load(response)

    resolved = str(data["info"]["version"])
    for entry in data["urls"]:
        if entry["packagetype"] == "bdist_wheel":
            return str(entry["url"]), resolved

    raise SystemExit(f"No wheel published on PyPI for zen-temple {resolved}.")


def _clear_explorer_dir() -> None:
    """Remove any previously fetched explorer files (the folder is gitignored)."""
    if not EXPLORER_DIR.exists():
        return
    for child in EXPLORER_DIR.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def _extract_explorer(blob: bytes) -> int:
    """Extract the explorer payload from a wheel archive. Returns file count."""
    count = 0
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        members = [
            name
            for name in archive.namelist()
            if name.startswith(WHEEL_PREFIX) and not name.endswith("/")
        ]
        if not members:
            raise SystemExit(
                "The downloaded wheel does not contain a zen_temple/explorer/ "
                "payload. Try a newer --version."
            )
        for name in members:
            relative = Path(name[len(WHEEL_PREFIX) :])
            destination = EXPLORER_DIR / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(name) as source, open(destination, "wb") as target:
                shutil.copyfileobj(source, target)
            count += 1
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version",
        default=None,
        help=(
            "zen-temple release to pull the explorer files from "
            "(default: latest release on PyPI)"
        ),
    )
    args = parser.parse_args()

    wheel_url, version = _resolve_wheel_url(args.version)
    print(f"Downloading zen-temple {version} wheel from PyPI ...")
    with urllib.request.urlopen(wheel_url) as response:  # noqa: S310 - https host
        blob = response.read()

    _clear_explorer_dir()
    EXPLORER_DIR.mkdir(parents=True, exist_ok=True)
    count = _extract_explorer(blob)

    print(f"Copied {count} files into {EXPLORER_DIR}")
    print("ZEN-explorer frontend is ready. Start the server with `zen-visualization`.")


if __name__ == "__main__":
    main()
