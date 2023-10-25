from sqlmodel import Session, create_engine
from sqlalchemy.exc import ArgumentError
from sqlalchemy.future.engine import Engine
from typing import Optional

# Load Models
from typing import Generator, Any
from src.config import config

try:
    engine: Optional[Engine] = create_engine(
        config.SQLALCHEMY_DATABASE_URL,
        connect_args={},
    )
except ArgumentError:
    engine = None


def get_session() -> Optional[Generator[Session, Any, Any]]:
    with Session(engine) as session:
        yield session
