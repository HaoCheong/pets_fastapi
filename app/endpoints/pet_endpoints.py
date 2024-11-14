''' Pet Endpoints

Contains all the function that subsequently call the Pet CRUD functions (see CRUD files)
Split was done because it allowed for simplified data validation and db calling.
- Endpoints: Takes in and validates input correctness
- CRUD: Focused on the logic of formatting and manipulating data, under the assumption that the provided data was correct

'''

from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.pet_cruds as cruds
import app.models.pet_models as models
from app.database.database import SessionDep

router = APIRouter()

@router.post("/pet/", response_model=models.PetReadNR, tags=['Pets'])
def create_pet(pet: models.PetCreate, db: SessionDep):
    db_pet = cruds.create_pet(db=db, new_pet=pet)
    return db_pet

@router.get("/pets/", response_model=list[models.PetReadNR], tags=['Pets'])
def get_all_pets(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    db_pets = cruds.get_all_pets(db=db, offset=offset, limit=limit)
    return db_pets

@router.get("/pet/{pet_id}", response_model=models.PetReadWR, tags=['Pets'])
def get_pet_by_id(pet_id: int, db: SessionDep):
    
    db_pet = cruds.get_pet_by_id(db=db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    return db_pet

@router.patch("/pet/{pet_id}", response_model=models.PetReadWR, tags=['Pets'])
def update_pet(pet_id: int, new_pet: models.PetUpdate, db: SessionDep):

    db_pet = cruds.get_pet_by_id(db=db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    return cruds.update_pet_by_id(db=db, pet_id=pet_id, new_pet=new_pet)

@router.delete("/pet/{pet_id}", tags=['Pets'])
def delete_pet(pet_id: int, db: SessionDep):
    
    db_pet = cruds.get_pet_by_id(db=db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    return cruds.delete_pet_by_id(db=db, pet_id=pet_id)
