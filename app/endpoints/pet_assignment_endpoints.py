''' Pet Assignment Endpoints

Contains all the function that subsequently call the pet assignment operations (see pet_assignment file)
Split was done because it allowed for simplified data validation and db calling.
- Endpoints: Takes in and validates input correctness
- CRUD: Focused on the logic of formatting and manipulating data, under the assumption that the provided data was correct

'''

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database.database import get_session

router = APIRouter()

import app.cruds.nutrition_plan_cruds as nutrition_plan_cruds
import app.cruds.owner_cruds as owner_cruds
import app.cruds.pet_assignment_cruds as pet_assignment_cruds
import app.cruds.pet_cruds as pet_cruds
import app.cruds.trainer_cruds as trainer_cruds

# ======== ASSIGNING PETS TO OWNER ========

@router.post("/assignToOwner/{pet_id}/{owner_id}", tags=["Item Assignments"])
def assign_pet_to_owner(pet_id: int, owner_id: int, db: Session = Depends(get_session)):
    db_owner = owner_cruds.get_owner_by_id(db, owner_id=owner_id)
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet already assigned to owner")

    return pet_assignment_cruds.assign_pet_to_owner(db, pet_id=pet_id, owner_id=owner_id)


@router.post("/unassignFromOwner/{pet_id}/{owner_id}", tags=["Item Assignments"])
def unassign_pet_from_owner(pet_id: int, owner_id: int, db: Session = Depends(get_session)):
    db_owner = owner_cruds.get_owner_by_id(db, owner_id=owner_id)
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet not in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to owner")

    return pet_assignment_cruds.unassign_pet_from_owner(db, pet_id=pet_id, owner_id=owner_id)

@router.post("/assignToNutritionPlan/{pet_id}/{nutrition_plan_id}", tags=["Item Assignments"])
def assign_pet_to_nutrition_plan(pet_id: int, nutrition_plan_id: int, db: Session = Depends(get_session)):
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)
    db_nutrition_plan = nutrition_plan_cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)

    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="Nutrition plan does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    # if len(db_pet.trainers) == 0:
    #     raise HTTPException(status_code=400, detail="Pets has not been assigned to trainer")
    
    if  db_pet.nutrition_plan is not None:
        raise HTTPException(
            status_code=400, detail="Pet already assigned to nutritional plan")
    
    return pet_assignment_cruds.assign_pet_to_nutrition_plan(db, pet_id=pet_id, nutrition_plan_id=nutrition_plan_id)


@router.post("/unassignFromNutritionPlan/{pet_id}", tags=["Item Assignments"])
def unassign_pet_from_nutrition_plan(pet_id: int, db: Session = Depends(get_session)):
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    if db_pet.nutrition_plan is None:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to nutritional plan")
    
    return pet_assignment_cruds.unassign_pet_from_nutrition_plan(db, pet_id=pet_id)

@router.post("/assignToTrainer/{pet_id}/{trainer_id}", tags=["Item Assignments"])
def assign_pet_to_trainer(pet_id: int, trainer_id: str, db: Session = Depends(get_session)):
    db_trainer = trainer_cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)

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

    return pet_assignment_cruds.assign_pet_to_trainer(db, pet_id=pet_id, trainer_id=trainer_id)


@router.post("/unassignFromTrainer/{pet_id}/{trainer_id}", tags=["Item Assignments"])
def unassign_pet_from_trainer(pet_id: int, trainer_id: str, db: Session = Depends(get_session)):
    db_trainer = trainer_cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)

    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet not in db_trainer.pets:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to trainer")

    return pet_assignment_cruds.unassign_pet_from_trainer(db, pet_id=pet_id, trainer_id=trainer_id)
