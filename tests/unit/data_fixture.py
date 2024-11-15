''' Data Fixtures

Contains all the necessary data for testing. All wrapped in Pytest Fixtures
'''

import pytest


@pytest.fixture
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


@pytest.fixture
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


@pytest.fixture
def pets_data():
    ''' Return test pets data '''
    return [
        {
            "name":"Pickles",
            "age": 2,
            "nickname": "The Gremlin"
        },
        {
            "name":"Rosie",
            "age": 1,
            "nickname": "The Sassy"
        },
        {
            "name":"Abbie",
            "age": 4,
            "nickname": "The Dancer"
        },
        {
            "name":"Cooper",
            "age": 3,
            "nickname": "The Biter"
        }
    ]


@pytest.fixture
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