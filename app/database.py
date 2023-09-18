"""Database.py (1)

Controls all the creation of the database

Terms:
 - SQLALCHEMY_DATABASE_URL: Location of the database (SQLITE3 in this case)
 - engine: Create a connection to the database
 - SessionLocal: A local instance of the database
"""

import pathlib
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ABS_PATH = pathlib.Path().resolve()
SQLALCHEMY_DATABASE_URL = f"sqlite:///{ABS_PATH}/app/db/pets.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
