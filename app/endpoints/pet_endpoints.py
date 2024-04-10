from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import app.schemas.pet_schemas as schemas
import app.cruds.pet_cruds as cruds

router = APIRouter()

@router.post("/api/v1/pet", response_model=schemas.PetReadNR, tags=["Pets"])
def create_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    return cruds.create_pet(db=db, pet=pet)


@router.get("/api/v1/pets", response_model=List[schemas.PetReadNR], tags=["Pets"])
def get_all_pets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_pets = cruds.get_all_pets(db, skip, limit)
    return db_pets


@router.get("/api/v1/pet/{pet_id}", response_model=schemas.PetReadWR, tags=["Pets"])
def get_pet_by_id(pet_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return db_pet


@router.patch("/api/v1/pet/{pet_id}", response_model=schemas.PetReadNR, tags=["Pets"])
def update_pet_by_id(pet_id: int, new_pet: schemas.PetUpdate, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return cruds.update_pet_by_id(db, id=pet_id, new_pet=new_pet)


@router.delete("/api/v1/pet/{pet_id}", tags=["Pets"])
def delete_pet_by_id(pet_id: int, db: Session = Depends(get_db)):
    db_pet = cruds.get_pet_by_id(db, id=pet_id)
    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    return cruds.delete_pet_by_id(db, id=pet_id)