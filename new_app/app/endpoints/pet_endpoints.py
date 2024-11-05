from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select

import app.cruds.pet_cruds as cruds
import app.models.pet_model as models
import app.schemas.pet_schemas as schemas
from app.database import get_session


SessionDep = Annotated[Session, Depends(get_session)]

router = APIRouter()

@router.post("/pet/", response_model=schemas.PetRead)
def create_pet(pet: schemas.PetCreate, session: SessionDep):

    db_pet = schemas.Pet.model_validate(pet)

    session.add(db_pet)
    session.commit()
    session.refresh(db_pet)

    return db_pet

@router.get("/pets/", response_model=list[schemas.PetRead])
def read_pets(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[schemas.Pet]:
    pet = session.exec(select(schemas.Pet).offset(offset).limit(limit)).all()
    return pet

@router.get("/pet/{pet_id}", response_model=list[schemas.PetRead])
def read_pet(pet_id: int, session: SessionDep):

    pet = session.get(schemas.Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    return pet

@router.patch("/pet/{pet_id}", response_model=schemas.PetRead)
def update_pet(pet_id: int, pet: schemas.PetUpdate, session: SessionDep):
    pet_db = session.get(schemas.Pet, pet_id)
    if not pet_db:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    pet_data = pet.model_dump(exclude_unset=True)
    pet_db.sqlmodel_update(pet_data)

    session.add(pet_db)
    session.commit()
    session.refresh(pet_db)

    return pet_db

@router.delete("/pet/{pet_id}")
def delete_pet(pet_id: int, session: SessionDep):

    pet = session.get(schemas.Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    session.delete(pet)
    session.commit()

    return {"Success": True}