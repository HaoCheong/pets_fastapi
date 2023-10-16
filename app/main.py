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
import app.metadata as metadata

from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

# Initialising instance of the backend
app = FastAPI(openapi_tags=metadata.tags_metadata)

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

@app.post("/owner", response_model=schemas.OwnerReadNR, tags=["Owners"])
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    return cruds.create_owner(db=db, owner=owner)


@app.get("/owner", response_model=List[schemas.OwnerReadNR], tags=["Owners"])
def get_all_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_owners = cruds.get_all_owners(db, skip, limit)
    return db_owners


@app.get("/owner/{owner_id}", response_model=schemas.OwnerReadWR, tags=["Owners"])
def get_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return db_owner


@app.patch("/owner/{owner_id}", response_model=schemas.OwnerReadNR, tags=["Owners"])
def update_owner_by_id(owner_id: int, new_owner: schemas.OwnerUpdate, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return cruds.update_owner_by_id(db, id=owner_id, new_owner=new_owner)


@app.delete("/owner/{owner_id}", tags=["Owners"])
def delete_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return cruds.delete_owner_by_id(db, id=owner_id)

# ======== PETS CRUD ENDPOINTS ========


@app.post("/pet", response_model=schemas.PetReadNR, tags=["Pets"])
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return cruds.create_pet(db=db, pet=pet)


@app.get("/pet", response_model=List[schemas.PetReadNR], tags=["Pets"])
def get_all_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_pets = cruds.get_all_pets(db, skip, limit)
    return db_pets


@app.get("/pet/{pet_id}", response_model=schemas.PetReadWR, tags=["Pets"])
def get_pet_by_id(pet_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return db_pet


@app.patch("/pet/{pet_id}", response_model=schemas.PetReadNR, tags=["Pets"])
def update_pet_by_id(pet_id: int, new_pet: schemas.PetUpdate, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return cruds.update_pet_by_id(db, id=pet_id, new_pet=new_pet)


@app.delete("/pet/{pet_id}", tags=["Pets"])
def delete_pet_by_id(pet_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return cruds.delete_pet_by_id(db, id=pet_id)

# ======== TRAINER CRUD ENDPOINTS ========


@app.post("/trainer", response_model=schemas.TrainerReadNR, tags=["Trainers"])
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer.trainer_id)
    if db_trainer:
        raise HTTPException(status_code=400, detail="Trainer already exist")

    return cruds.create_trainer(db=db, trainer=trainer)


@app.get("/trainer", response_model=List[schemas.TrainerReadNR], tags=["Trainers"])
def get_all_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_trainers = cruds.get_all_trainers(db, skip, limit)
    return db_trainers


@app.get("/trainer/{trainer_id}", response_model=schemas.TrainerReadWR, tags=["Trainers"])
def get_trainer_by_id(trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return db_trainer


@app.patch("/trainer/{trainer_id}", response_model=schemas.TrainerReadNR, tags=["Trainers"])
def update_trainer_by_id(trainer_id: str, new_trainer: schemas.TrainerUpdate, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return cruds.update_trainer_by_id(db, trainer_id=trainer_id, new_trainer=new_trainer)


@app.delete("/trainer/{trainer_id}", tags=["Trainers"])
def delete_trainer_by_id(trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return cruds.delete_trainer_by_id(db, trainer_id=trainer_id)

# ======== NUTRITION PLAN CRUD ENDPOINTS ========

@app.post("/nutrition_plan", response_model=schemas.NutritionPlanReadNR, tags=["Nutrition Plans"])
def create_nutrition_plan(nutrition_plan: schemas.NutritionPlanCreate, db: Session = Depends(get_db)):
    return cruds.create_nutrition_plan(db=db, nutrition_plan=nutrition_plan)


@app.get("/nutrition_plans", response_model=List[schemas.NutritionPlanReadNR], tags=["Nutrition Plans"])
def get_all_nutrition_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_nutrition_plans = cruds.get_all_nutrition_plans(db, skip, limit)
    return db_nutrition_plans


@app.get("/nutrition_plan/{nutrition_plan_id}", response_model=schemas.NutritionPlanReadWR, tags=["Nutrition Plans"])
def get_nutrition_plan_by_id(nutrition_plan_id: str, db: Session = Depends(get_db)):
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)
    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="Nutrition plan does not exist")

    return db_nutrition_plan


@app.patch("/nutrition_plan/{nutrition_plan_id}", response_model=schemas.NutritionPlanReadWR, tags=["Nutrition Plans"])
def update_nutrition_plan_by_id(nutrition_plan_id: str, new_nutrition_plan: schemas.NutritionPlanUpdate, db: Session = Depends(get_db)):
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)
    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="Nutrition plan does not exist")

    return cruds.update_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id, new_nutrition_plan=new_nutrition_plan)


@app.delete("/nutrition_plan/{nutrition_plan_id}", tags=["Nutrition Plans"])
def delete_nutrition_plan_by_id(nutrition_plan_id: str, db: Session = Depends(get_db)):
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)
    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="nutrition_plan does not exist")

    return cruds.delete_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)


# ======== ASSIGNING PETS TO OWNER ========


@app.post("/assignToOwner/{pet_id}/{owner_id}", tags=["Item Assignments"])
def assign_pet_to_owner(pet_id: int, owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet already assigned to owner")

    return cruds.assign_pet_to_owner(db, pet_id=pet_id, owner_id=owner_id)


@app.post("/unassignToOwner/{pet_id}/{owner_id}", tags=["Item Assignments"])
def unassign_pet_from_owner(pet_id: int, owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet not in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to owner")

    return cruds.unassign_pet_from_owner(db, pet_id=pet_id, owner_id=owner_id)

# ======== ASSIGNING PETS TO TRAINER ========


@app.post("/assignToTrainer/{pet_id}/{trainer_id}", tags=["Item Assignments"])
def assign_pet_to_trainer(pet_id: int, trainer_id: str, db: Session = Depends(get_db)):
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

    return cruds.assign_pet_to_trainer(db, pet_id=pet_id, trainer_id=trainer_id)


@app.post("/unassignToTrainer/{pet_id}/{trainer_id}", tags=["Item Assignments"])
def unassign_pet_from_trainer(pet_id: int, trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet not in db_trainer.pets:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to trainer")

    return cruds.unassign_pet_from_trainer(db, pet_id=pet_id, trainer_id=trainer_id)

@app.post("/assignToNutritionPlan/{pet_id}/{nutrition_plan_id}", tags=["Item Assignments"])
def assign_pet_to_nutrition_plan(pet_id: int, nutrition_plan_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)

    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="Nutrition plan does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    if  db_pet.nutrition_plan is not None:
        raise HTTPException(
            status_code=400, detail="Pet already assigned to nutritional plan")
    
    return cruds.assign_pet_to_nutrition_plan(db, pet_id=pet_id, nutrition_plan_id=nutrition_plan_id)

@app.post("/unassignToNutritionPlan/{pet_id}", tags=["Item Assignments"])
def unassign_pet_from_nutrition_plan(pet_id: int, nutrition_plan_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    if db_pet.nutrition_plan is None:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to nutritional plan")
    
    return cruds.unassign_pet_from_nutrition_plan(db, pet_id=pet_id)