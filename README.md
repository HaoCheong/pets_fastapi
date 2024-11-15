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
1. `tests/unit/conftest.py`
2. `tests/unit/wrappers.py`
3. `tests/unit/*_test.py`

## Setting Up

### Local

If you want to auto-install all of the dependencies:
```
pip3 install -r requirements.txt
```

### Building Docker Container

You can build an image of the app as a docker container. Assuming you have docker install. Run the following script:

```
./build_containers.sh
```


## Start up

### Run locally

To start the server, after installing all the dependencies while in the root folder for this project `/pets_fastapi`, run:
```
//To run in development mode (with hot reload)
fastapi dev app/main.py

//To run in production mode
fastapi run app/main.py
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view Swagger Docs

### Running Container

> [!warning]
> Docker container uses port number 9991 where as by default, running locally uses port number 8000

After building the docker container image, run the following script to run the container

```
./run_containers.sh
```
Visit [http://127.0.0.1:9991/docs](http://127.0.0.1:9991/docs) to view Swagger Docs

## Testing

There are testing functions that have been provided.
1. **Populate**: A simple function that populates a database when the webserver is running. Used to populate the database based on a following structure
2. **Unit**: A set of unit tests to test each endpoint in the project. Built using the Pytest library.

### Populate
To run the data populator, first start the webserver (see Start Up Section) and run following commands in the separate terminal in the root folder for this project `/pets_fastapi`:

```
python3 tests/populate/populate.py
```

It will generate a data set that have the following relationship seen in the diagram below.

![Test data structure layout](image.png)

### Unit
To run every unit tests, run the following script:
```
./run_test.sh
```

To run specific tests, run the following command
```
python3 -m pytest tests/unit/<test_file>.py -s -k <test_function_name>
```

