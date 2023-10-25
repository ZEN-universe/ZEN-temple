from src.routers import cases, solutions
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import src.utils.updates

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/public", StaticFiles(directory="public", follow_symlink=True), name="public"
)

app.include_router(cases.router)
app.include_router(solutions.router)

try:
    src.utils.updates.update_database()
except Exception:
    print("Could not update database, skipping.")

src.utils.updates.create_components()
