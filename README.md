# FASTAPI TUTORIAL BACKEND

This is a tutorial backend for those trying to understand and learn FastAPI.
It contains the basics to start creating a full fledge FastAPI backend!

Contains learning how to apply SQLAlchemy to different DB relationships:
- Many-to-Many relationship via Association Object
- One-to-Many relationship

## Premise

There is pet owner and pet training system.
- Pets data be created, viewed, updated and deleted
- Owner data be created, viewed, updated and deleted
- Trainer data be created, viewed, updated and deleted

- Pets can only be assigned to 1 owner
- Owners can be assigned as many pets

- Pets can be assigned to many trainers
- Trainers can be assigned to many pets

- Trainers ID can be updated. Pet and Owner ID cannot

## Learning order

The order to go through the files is as follows:
1. database.py
2. models.py
3. schemas.py
4. cruds.py
5. main.py

## Setting Up

If you have not installed fastapi:
```
pip3 install "fastapi[all]"
```

If you have not installed SQLITE3 before:
```
pip3 install sqlite3
```

If you have not installed SQLAlchemy before:
```
pip3 install SQLAlchemy
```

## Start up

To start the server, run:
```
uvicorn main:app --reload
```
or if you want to specify a port
```
uvicorn main:app --reload --port 8001
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view Swagger Docs
