"""main.py (5)

Where the endpoints are instantiated and functions are called

- All the data validation are checked here
- Error raising done on this level

"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import app.cruds as cruds
import app.models as models
import app.schemas as schemas

from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

# Initialising instance of the backend
app = FastAPI()

# Handles CORS, currently available to any origin. Need to be tweaked for security
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Gets an instance of the DB, will close connection with DB when done


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ======== ROOT ENDPOINT ========
# Not necessary but good indication that connection been made


@app.get("/")
def root():
    return {"connection": True}


# ======== OWNER CRUD ENDPOINTS ========

@app.post("/owner", response_model=schemas.OwnerReadNR)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    return cruds.create_owner(db=db, owner=owner)


@app.get("/owner", response_model=List[schemas.OwnerReadNR])
def get_all_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_owners = cruds.get_all_owners(db, skip, limit)
    return db_owners


@app.get("/owner/{owner_id}", response_model=schemas.OwnerReadWR)
def get_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return db_owner


@app.patch("/owner/{owner_id}", response_model=schemas.OwnerReadNR)
def update_owner_by_id(owner_id: int, new_owner: schemas.OwnerUpdate, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return cruds.update_owner_by_id(db, id=owner_id, new_owner=new_owner)


@app.delete("/owner/{owner_id}")
def delete_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return cruds.delete_owner_by_id(db, id=owner_id)

# ======== PETS CRUD ENDPOINTS ========


@app.post("/pet", response_model=schemas.PetReadNR)
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return cruds.create_pet(db=db, pet=pet)


@app.get("/pet", response_model=List[schemas.PetReadNR])
def get_all_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_pets = cruds.get_all_pets(db, skip, limit)
    return db_pets


@app.get("/pet/{pet_id}", response_model=schemas.PetReadWR)
def get_pet_by_id(pet_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return db_pet


@app.patch("/pet/{pet_id}", response_model=schemas.PetReadNR)
def update_pet_by_id(pet_id: int, new_pet: schemas.PetUpdate, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return cruds.update_pet_by_id(db, id=pet_id, new_pet=new_pet)


@app.delete("/pet/{pet_id}")
def delete_pet_by_id(pet_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return cruds.delete_pet_by_id(db, id=pet_id)

# ======== TRAINER CRUD ENDPOINTS ========


@app.post("/trainer", response_model=schemas.TrainerReadNR)
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer.trainer_id)
    if db_trainer:
        raise HTTPException(status_code=400, detail="Trainer already exist")

    return cruds.create_trainer(db=db, trainer=trainer)


@app.get("/trainer", response_model=List[schemas.TrainerReadNR])
def get_all_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_trainers = cruds.get_all_trainers(db, skip, limit)
    return db_trainers


@app.get("/trainer/{trainer_id}", response_model=schemas.TrainerReadWR)
def get_trainer_by_id(trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return db_trainer


@app.patch("/trainer/{trainer_id}", response_model=schemas.TrainerReadNR)
def update_trainer_by_id(trainer_id: str, new_trainer: schemas.TrainerUpdate, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return cruds.update_trainer_by_id(db, trainer_id=trainer_id, new_trainer=new_trainer)


@app.delete("/trainer/{trainer_id}")
def delete_trainer_by_id(trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return cruds.delete_trainer_by_id(db, trainer_id=trainer_id)

# ======== ASSIGNING PETS TO OWNER ========


@app.post("/assignToOwner/{pet_id}/{owner_id}")
def assignToOwner(pet_id: int, owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet already assigned to owner")

    return cruds.assignToOwner(db, pet_id=pet_id, owner_id=owner_id)


@app.post("/unassignToOwner/{pet_id}/{owner_id}")
def unassignToOwner(pet_id: int, owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet not in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to owner")

    return cruds.unassignFromOwner(db, pet_id=pet_id, owner_id=owner_id)

# ======== ASSIGNING PETS TO TRAINER ========


@app.post("/assignToTrainer/{pet_id}/{trainer_id}")
def assignToTrainer(pet_id: int, trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet.owner_id == None:
        raise HTTPException(
            status_code=400, detail="Pet does not have an owner")

    if db_pet in db_trainer.pets:
        raise HTTPException(
            status_code=400, detail="Pet already assigned to trainer")

    return cruds.assignToTrainer(db, pet_id=pet_id, trainer_id=trainer_id)


@app.post("/unassignToTrainer/{pet_id}/{trainer_id}")
def unassignToTrainer(pet_id: int, trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet not in db_trainer.pets:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to trainer")

    return cruds.unassignFromTrainer(db, pet_id=pet_id, trainer_id=trainer_id)
