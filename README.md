# PET FITNESS - A FastAPI Reference Backend (Version 1.1)

This is a tutorial backend for those trying to understand and learn FastAPI as well as a reference project
It contains the basics to start creating a full fledge FastAPI backend as well as understanding the fundamentals of Pytest!

Pre-requisite:
- Python knowledge

## Premise

*Welcome to Pet Fitness where you can train your pets by our very own, and very talented Trainers!*
*Our world class trainers will design a unique nutrition plan for every single one of you pets!*
*All you have to do is register you, your pets, and we will have one of our very own trainers evaluate your fuzzy little (or big) friends!*

> "Training a dog is like teaching a 2-year-old to clean their room. Good luck with that." ~ Anonymous

## Project Structure

Each Model has its own set of CRUD features
- Pets data be created, viewed, updated and deleted
- Owner data be created, viewed, updated and deleted
- Trainer data be created, viewed, updated and deleted
- Nutrition Plan created, viewed, updated and deleted

Contains learning how to apply SQLAlchemy to different DB relationships:
- Multiple Pets can belong to one Owner (One-to-Many relationship)
- Multiple pets can be trained by multiple trainer (Many-to-Many relationship via Association Object)
- Each pet can be on one unique nutrition plan at a time (One-to-One relationship)

There are also dependencies in the order of which pets are assigned.
- A pet can be assigned an owner
- A pet can be assigned an trainer, only if they are assigned to an owner
- A pet can be assigned a nutrition plan, only if they are assigned to a trainer

## Learning order

Depending on what you want to learn, certain files and directories can be ignored
Each significant directory and file have be annotated as well as the order of which to lean

### Basics of RestAPI Developement
1. `app/database/database.py`
2. `app/models`
3. `app/cruds`
4. `app/endpoints`
5. `app/main.py`

### Basics of PyTest writing
1. `tests/unit/client_fixtures.py`
2. `tests/unit/data_fixtures.py`
3. `tests/unit/wrappers.py`
4. `tests/unit/*_tests.py`

## Local - Setting Up and Running 

If you want to auto-install all of the dependencies:
```bash
# Setup a Virtual Environment
python3 -v venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the all the necessary requirements
pip3 install -r requirements.txt

# After shutting down the server, deactivate the virtual environment
source deactivate 
```

To start the server, after installing all the dependencies while in the root folder for this project `/pets_fastapi`, run:

```bash
//To run in development mode (with hot reload)
fastapi dev app/main.py

//To run in production mode
fastapi run app/main.py
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view Swagger Docs

## Docker - Setting Up and Running

Two scripts are provided to help testing and running the containers:
- `run_demo.sh`: Contains all the necessary scripts to run demo instances of the containers as well as unit tests. Uses PostgreSQL docker instances for easy data testing and resetting
- `run_live.sh`: Similar to demo but explicitly made to run live/production instances

At the top of each script there are configurations that are to be set. Working example values have been provided for both demo and live versions

```bash
# vvvvvvvvvvvvvvvvvvvv CONFIGURATION vvvvvvvvvvvvvvvvvvvv

PROJECT_NAME="Pets FastAPI Demo"
LOCAL_PROJECT_PATH=/home/hcheong/Desktop/Other/pets_fastapi

PETS_POSTGRES_DB_USER="demo_pets_user"
PETS_POSTGRES_DB_PASS="demo_pets_pass"
PETS_POSTGRES_DB_NAME="demo_pets_database"
PETS_POSTGRES_DB_HOST="10.1.50.133"
PETS_POSTGRES_DB_PORT="8581"
PETS_SQL_DUMP_FILE_PATH="${LOCAL_PROJECT_PATH}/utils/test_pets_dump.sql"
PETS_SQL_DUMP_SCHEMA_ONLY=0
PETS_CONTAINER_NAME="pets_demo_database_cont"
PETS_IMAGE_NAME="postgres:14.5"
PETS_TIMEZONE="Australia/Sydney"

BACKEND_PORT=8582
BACKEND_APP_PATH="${LOCAL_PROJECT_PATH}"
BACKEND_CONTAINER_URL="http://${PETS_POSTGRES_DB_HOST}:${BACKEND_PORT}"
BACKEND_CONTAINER_NAME="pets_fastapi_demo_backend_cont"
BACKEND_IMAGE_NAME="pets_fastapi_backend_img"
BACKEND_TIMEZONE="Australia/Sydney"

BACKEND_ENV="${LOCAL_PROJECT_PATH}/.venv"

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```

Once the configuration is set, you can run an a live instance using the following command:

```bash
./run_live.sh start
```

More commands are provided for you to better control the docker startup, see all the commands by running the following command:

```bash
./run_live.sh help
```

You can also run a demo instance using the following command:

```bash
./run_demo.sh demo
```
More commands are provided for you to better control the docker startup, see all the commands by running the following command:

```bash
./run_demo.sh help
```

## Testing

### Running a Demo

You can run a demo instance for testing.

A test dump sql file has been provided in `utils/test_pets_dump.sql` containing test data to allow for easy demoing of the application.
Prior to running the demo, these configurations can be changed to set up how the demo starts.

To run an instance of the database with no tables (tables will be generated when the project start), set the following configurations as follows:

```bash
PETS_SQL_DUMP_FILE_PATH=""
PETS_SQL_DUMP_SCHEMA_ONLY=0
```

To run an instance of the database with the tables but no test data, set the following configurations as follows:

```bash
PETS_SQL_DUMP_FILE_PATH="${LOCAL_PROJECT_PATH}/utils/test_pets_dump.sql"
PETS_SQL_DUMP_SCHEMA_ONLY=1
```

To run an instance of the database with the test data, set the following configurations as follows

```bash
PETS_SQL_DUMP_FILE_PATH="${LOCAL_PROJECT_PATH}/utils/test_pets_dump.sql"
PETS_SQL_DUMP_SCHEMA_ONLY=0
```

It will generate a data set that have the following relationship seen in the diagram below.

![Test data structure layout](image.png)

You are free to dump your own testing data yourself, just replace `test_pets_dump.sql` with your own .sql file dump

To start the demo, run the following command

```bash
./run_demo.sh demo
```

### Unit

To run every unit tests, run the following script:

```bash
./run_demo.sh unit
```

