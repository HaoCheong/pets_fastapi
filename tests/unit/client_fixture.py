'''client_fixture.py

Contains all the necessary processes to create a sqlalchemy compatible testing client
'''

from typing import Annotated

import pytest

from fastapi import Depends
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from app.main import app
from app.database.database import get_session


sqlite_file_name = "app/database/test_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    ''' Instantiate the database tables '''
    SQLModel.metadata.create_all(engine)

def override_get_session():
    with Session(engine) as session:
        yield session

# Overiddes a dependency function with another function
app.dependency_overrides[get_session] = override_get_session

client = TestClient(app)

SUCCESS = 200
ERROR = 400
NOT_FOUND = 404


@pytest.fixture
def reset_db():
    ''' Resets the database via dropping '''
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)