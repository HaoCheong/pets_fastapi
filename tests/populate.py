''' Populate

Auto-populates a database with test data.

- Great for debugging especially when the data structure is known
- Easy control over the database data
- Used separately to unit test, populate is used when you want to do manual testing instead
'''

import requests

BACKEND_URL = "http://10.1.50.133:8582/api/v1"

PETS = [
    {
        "name": "Pickles",
        "age": 2,
        "nickname": "The Gremlin"
    },
    {
        "name": "Rosie",
        "age": 1,
        "nickname": "The Sassy"
    },
    {
        "name": "Abbie",
        "age": 4,
        "nickname": "The Dancer"
    },
    {
        "name": "Cooper",
        "age": 3,
        "nickname": "The Biter"
    }
]

OWNERS = [
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

TRAINERS = [
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

NUTRITION_PLANS = [
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


def populate_pets():
    ''' Populates database with pets data '''
    print("========== ADDING PETS ==========")
    for pet in PETS:
        try:
            res = requests.post(f"{BACKEND_URL}/pet", json=pet)
            if res.status_code != 200:
                raise ValueError

            print("Added PETS - %s" % pet)
        except ValueError:
            print("Failed to add PETS - %s" % pet)


def populate_owners():
    ''' Populates database with owner data '''
    print("========== ADDING OWNERS ==========")
    for owner in OWNERS:
        try:
            res = requests.post(f"{BACKEND_URL}/owner", json=owner)
            if res.status_code != 200:
                raise ValueError

            print("Added OWNER - %s" % owner)
        except ValueError:
            print("Failed to add OWNER - %s" % owner)


def populate_trainers():
    ''' Populates database with trainer data '''
    print("========== ADDING TRAINERS ==========")
    for trainer in TRAINERS:
        try:
            res = requests.post(f"{BACKEND_URL}/trainer", json=trainer)
            if res.status_code != 200:
                raise ValueError

            print("Added TRAINER - %s" % trainer)
        except ValueError:
            print("Failed to add TRAINER - %s" % trainer)


def populate_nutrition_plans():
    ''' Populates database with nutrition plan data '''
    print("========== ADDING NUTRITIONAL PLAN ==========")
    for n_plan in NUTRITION_PLANS:
        try:
            res = requests.post(f"{BACKEND_URL}/nutrition_plan", json=n_plan)
            if res.status_code != 200:
                raise ValueError

            print("Added NUTRITION PLAN - %s" % n_plan)
        except ValueError:
            print("Failed to add NUTRITION PLAN - %s" % n_plan)


def assigning_pets_to_owner():
    ''' Handles assignment of pets to owners '''
    print("========== ASSIGNING PETS TO OWNER ==========")

    print("Assigning Pickles to Alice")
    res = requests.post(f"{BACKEND_URL}/assignToOwner/1/1")

    print("Assigning Rosie to Alice")
    res = requests.post(f"{BACKEND_URL}/assignToOwner/2/1")

    print("Assigning Abbie to Alice")
    res = requests.post(f"{BACKEND_URL}/assignToOwner/3/1")

    print("Assigning Cooper to Bob")
    res = requests.post(f"{BACKEND_URL}/assignToOwner/4/2")


def assigning_pets_to_trainer():
    ''' Handles assignment of pets to trainers '''
    print("========== ASSIGNING PETS TO TRAINER ==========")

    print("Assigning Pickles to Eddie Bark")
    res = requests.post(f"{BACKEND_URL}/assignToTrainer/1/TR-013")

    print("Assigning Rosie to Eddie Bark")
    res = requests.post(f"{BACKEND_URL}/assignToTrainer/2/TR-013")

    print("Assigning Abbie to Lara Meowstein")
    res = requests.post(f"{BACKEND_URL}/assignToTrainer/3/TR-047")

    print("Assigning Pickles to Eddie Bark")
    res = requests.post(f"{BACKEND_URL}/assignToTrainer/4/TR-013")


def assigning_pets_to_nutrition_plan():
    ''' Handles assignment of pets to nutritional plan '''
    print("========== ASSIGNING PETS TO NUTRITION PLAN ==========")

    print("Assigning Pickles to Pickles Meal Deal")
    res = requests.post(f"{BACKEND_URL}/assignToNutritionPlan/1/1")

    print("Assigning Rosie to Rosie Roast Plan")
    res = requests.post(f"{BACKEND_URL}/assignToNutritionPlan/2/2")

    print("Assigning Cooper to Cooper Card Load")
    res = requests.post(f"{BACKEND_URL}/assignToNutritionPlan/4/3")


if __name__ == "__main__":

    populate_owners()
    populate_pets()
    populate_trainers()
    populate_nutrition_plans()
#
    assigning_pets_to_owner()
    assigning_pets_to_trainer()
    assigning_pets_to_nutrition_plan()
