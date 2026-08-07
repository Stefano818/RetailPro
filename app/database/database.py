import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is not configured in .env"
    )


if DATABASE_URL.startswith("sqlite:///"):

    database_path = DATABASE_URL.replace(
        "sqlite:///",
        "",
        1,
    )

    database_file = Path(database_path)


    if database_file.parent:

        database_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )



engine = create_engine(
    DATABASE_URL,
    echo=False,

    connect_args={
        "check_same_thread": False
    }
    if DATABASE_URL.startswith("sqlite")
    else {},
)



SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)