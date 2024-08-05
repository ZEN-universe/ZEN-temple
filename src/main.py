from src.routers import solutions
from collections.abc import AsyncIterator

import uvicorn

from contextlib import asynccontextmanager

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
import webbrowser


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    FastAPICache.init(InMemoryBackend())
    yield


app = FastAPI(lifespan=lifespan)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # type: ignore
    allow_credentials=True,  # type: ignore
    allow_methods=["*"],  # type: ignore
    allow_headers=["*"],  # type: ignore
)

app.include_router(solutions.router)
app.mount("/explorer", StaticFiles(directory="explorer", html=True), name="explorer")

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=8000, log_level="info")
    server = uvicorn.Server(config)
    webbrowser.open('http://localhost:8000/explorer', new=2)

    server.run()

