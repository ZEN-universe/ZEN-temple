from .routers import solutions
from collections.abc import AsyncIterator

import uvicorn

from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
import webbrowser
import os


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    FastAPICache.init(InMemoryBackend())
    yield


app = FastAPI(lifespan=lifespan)

apiapp = FastAPI()
apiapp.include_router(solutions.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # type: ignore
    allow_credentials=True,  # type: ignore
    allow_methods=["*"],  # type: ignore
    allow_headers=["*"],  # type: ignore
)

app.mount("/api", apiapp)

explorer_path = os.path.join(os.path.dirname(__file__), "explorer")
app.mount("/", StaticFiles(directory=explorer_path, html=True), name="explorer")
config = uvicorn.Config("main:app", port=8000, log_level="info")
server = uvicorn.Server(config)

if __name__ == "__main__":
    webbrowser.open("http://localhost:8000/", new=2)
    server.run()
