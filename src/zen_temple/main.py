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
app.mount(explorer_url, StaticFiles(directory=explorer_path, html=True), name="explorer")

def start_server(solution_folder: str, port: int, app_name: str | None = None, api_url: str | None = None, reload: bool = False):
    if api_url is None:
        api_url = f"http://127.0.0.1:{port}/api/"
    if app_name is None:
        app_name = ""

    config.SOLUTIONS_FOLDER = solution_folder
    
    env_file = Path(__file__).parent / "explorer" / "_app" / "env.js"
    with open(env_file, 'w') as file:
        file.write(f'export const env={{"PUBLIC_TEMPLE_URL":"{api_url}", "PUBLIC_APP_NAME":"{app_name}"}}')

    # Define uvicorn settings
    print("Starting server...")
    uvicorn_config = uvicorn.Config("src.zen_temple.main:app", port=port, log_level="info", reload=reload)
    server = uvicorn.Server(uvicorn_config)

    webbrowser.open(f"http://localhost:{port}/", new=2)
    server.run()

def parse_arguments_and_run():
    args = ArgumentParser(description="ZEN Temple - Visualization web platform for ZEN Garden")
    
    group = args.add_argument_group("Server Options")
    group.add_argument("-p", "--port", required=False, type=int, default=8000, help="specify port to run the server on")
    group.add_argument("--solution_folder", required=False, type=str, default="./outputs", help="specify path to the solution folder [default=./output]")
    
    group = args.add_argument_group("Developer Options")
    group.add_argument("--app_name", required=False, type=str, default="", help="set the name of the app")
    group.add_argument("--api_url", required=False, type=str, default=None, help="set URL to the API to fetch the data from")
    group.add_argument("--reload", required=False, action="store_true", help="enable reload for development purposes")
    args = args.parse_args()
    
    start_server(args.solution_folder, args.port, args.app_name, args.api_url, args.reload)

if __name__ == "__main__":
    parse_arguments_and_run()
