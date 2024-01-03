"""Database.py (1)

Controls all the creation of the database

Terms:
 - SQLALCHEMY_DATABASE_URL: Location of the database (SQLITE3 in this case)
 - engine: Create a connection to the database
 - SessionLocal: A local instance of the database
"""

import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

# Grabs the absolute path of this files location
# Thus making this code agnostic to whatever file structure you are on
ABS_PATH = pathlib.Path().resolve()
SQLALCHEMY_DATABASE_URL = f"sqlite:///{ABS_PATH}/new_app/db/pets_2.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass