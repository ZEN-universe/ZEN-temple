from src.routers import solutions
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import src.utils.updates

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # type: ignore
    allow_credentials=True,  # type: ignore
    allow_methods=["*"],  # type: ignore
    allow_headers=["*"],  # type: ignore
)

app.mount(
    "/public", StaticFiles(directory="public", follow_symlink=True), name="public"
)

app.include_router(solutions.router)
"""
try:
    src.utils.updates.update_database()
except Exception:
    print("Could not update database, skipping.")

src.utils.updates.create_components()
"""
