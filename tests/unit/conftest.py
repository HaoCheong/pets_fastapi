'''conftest.py

Contains helpers, test client and pytest fixtures to be reused in automated unit testing

- Fixtures can be thought of reusable functions for unit testing
- Test client is a fake client used to emulate the client in production without affecting production data
'''

from app.database import Base
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
import pytest
from app.helpers import get_db
from app.main import app

import pathlib
 
# Creates an initial engine that does point to production
ABS_PATH = pathlib.Path().resolve()
SQLALCHEMY_DATABASE_URL = f"sqlite:///{ABS_PATH}/app/db/pets.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Overiddes the database with a testing database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Overiddes a dependency function with another function
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

SUCCESS = 200
ERROR = 400


@ pytest.fixture
def reset_db():
    ''' Resets the database via dropping '''
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@ pytest.fixture
def owners_data():
    ''' Return test owner data '''
    return [
        {
            "name": "Alice",
            "email": "alice@bigpond.com",
            "home_address": "Unit 1, 124 Copernicus Avenue",
            "password": "iLovePuppies123!"
        },
        {
            "name": "Bob",
            "email": "bob@ymail.com",
            "home_address": "912 Dylan Lane",
            "password": "pattingGiver381"
        }
    ]

@ pytest.fixture
def trainers_data():
    ''' Return test trainer data '''
    return [
        {
            "name": "Eddie Bark",
            "description": "Export in pet cardio",
            "phone_no": "04442123123",
            "email": "eddie.bark@plusWoofers.com",
            "date_started": "2021-01-07T00:00:00.000Z",
            "trainer_id": "TR-013",
        },
        {
            "name": "Lara Meowstein",
            "description": "Professional pet bodybuilding coach",
            "phone_no": "0333789789",
            "email": "lara.meowstein@plusWoofers.com",
            "date_started": "2019-12-31T00:00:00.000Z",
            "trainer_id": "TR-047",
        }
    ]

@ pytest.fixture
def pets_data():
    ''' Return test pets data '''
    return [
        {
            "name":"Pickles",
            "age": 2
        },
        {
            "name":"Rosie",
            "age": 1
        },
        {
            "name":"Abbie",
            "age": 4
        },
        {
            "name":"Cooper",
            "age": 3
        }
    ]

@ pytest.fixture
def nutrition_plans_data():
    ''' Return test nutrition plan data '''
    return [
        {
            "name": "Pickles Meal Deal",
            "description": "High vitamin meal with low carbs",
            "meal": {
                "protein": "Chicken",
                "carb": "Brown Rice",
                "fibre": "Broccolli"
            },
            "starting_date": "2023-10-10T00:00:00.000Z",
        },
        {
            "name": "Rosie Roast Plan",
            "description": "High protein for the aspiring competitor",
            "meal": {
                "protein": "Beef",
                "carb": "Dog Pasta",
                "fibre": "Beans"
            },
            "starting_date": "2023-08-23T00:00:00.000Z",
        },
        {
            "name": "Cooper Carb Load",
            "description": "Dense carb plan for a picky eater",
            "meal": {
                "protein": "Fish",
                "carb": "Puppy Penne",
                "fibre": "Corn"
            },
            "starting_date": "2021-03-03T00:00:00.000Z",
        },

    ]

