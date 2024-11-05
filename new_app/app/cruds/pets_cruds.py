from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

import app.schemas.pets_schemas as schemas
import app.models.pets_models as models

def create_pet(db: Session, new_pet: schemas.PetCreate):
    
    db_pet = schemas.Pet.model_validate(new_pet)

    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)

    return db_pet

def get_all_pets(db: Session, offset: int = 0, limit: int = 100):
    pet = db.exec(select(schemas.Pet).offset(offset).limit(limit)).all()
    return pet

def get_pet_by_id(db: Session, pet_id: int):

    pet = db.get(schemas.Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    return pet

def update_pet_by_id(db: Session, pet_id: int, new_pet: schemas.PetUpdate):
    pet_db = db.get(schemas.Pet, pet_id)
    
    if not pet_db:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    pet_data = new_pet.model_dump(exclude_unset=True)
    pet_db.sqlmodel_update(pet_data)

    db.add(pet_db)
    db.commit()
    db.refresh(pet_db)

    return pet_db

def delete_pet_by_id(db: Session, pet_id: int):
    pet = db.get(schemas.Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    db.delete(pet)
    db.commit()

    return {"Success": True}