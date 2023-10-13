from sqlmodel import Session, create_engine

# Load Models
from typing import Generator, Any
from src.config import config


engine = create_engine(
    config.SQLALCHEMY_DATABASE_URL,
    connect_args={},
)


def get_session() -> Generator[Session, Any, Any]:
    with Session(engine) as session:
        yield session
