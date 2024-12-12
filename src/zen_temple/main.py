import os
import webbrowser

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routers import solutions

# Initialize default app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # type: ignore
    allow_credentials=True,  # type: ignore
    allow_methods=["*"],  # type: ignore
    allow_headers=["*"],  # type: ignore
)


# Initialize api app
api_app = FastAPI()
api_app.include_router(solutions.router)
app.mount("/api", api_app)

# Mount explorer as static files
explorer_path = os.path.join(os.path.dirname(__file__), "explorer")
explorer_url = "/"
app.mount(explorer_url, StaticFiles(directory=explorer_path, html=True), name="explorer")

# Define uvicorn settings
config = uvicorn.Config("main:app", port=8000, log_level="info")
server = uvicorn.Server(config)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8000/", new=2)
    server.run()
