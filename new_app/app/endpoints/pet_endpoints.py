from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.pet_cruds as cruds
import app.schemas.pet_schemas as schemas
from app.database.database import SessionDep, create_db_and_tables

router = APIRouter()


@router.on_event("startup")
def on_startup():
    create_db_and_tables()


@router.post("/pet/", response_model=schemas.PetRead, tags=['Pets'])
def create_pet(pet: schemas.PetCreate, db: SessionDep):
    db_pet = cruds.create_pet(db=db, new_pet=pet)
    return db_pet

@router.get("/pets/", response_model=list[schemas.PetRead], tags=['Pets'])
def get_all_pets(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[schemas.Pet]:
    db_pets = cruds.get_all_pets(db=db, offset=offset, limit=limit)
    return db_pets

@router.get("/pet/{pet_id}", response_model=schemas.PetRead, tags=['Pets'])
def get_pet_by_id(pet_id: int, db: SessionDep):
    
    db_pet = cruds.get_pet_by_id(db=db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=400, detail="Pet does not exist")
    
    return db_pet

@router.patch("/pet/{pet_id}", response_model=schemas.PetRead, tags=['Pets'])
def update_pet(pet_id: int, new_pet: schemas.PetUpdate, db: SessionDep):

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