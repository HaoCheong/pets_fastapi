from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query, APIRouter
from sqlmodel import Field, Session, SQLModel, create_engine, select

import app.schemas.pets_schemas as schemas

from app.database import create_db_and_tables 
router = APIRouter()


@router.on_event("startup")
def on_startup():
    create_db_and_tables()


@router.post("/pet/", response_model=schemas.PetRead)
def create_pet(pet: schemas.PetCreate, db: SessionDep):
    pass
    

@router.get("/pets/", response_model=list[schemas.PetRead])
def get_all_pets(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[Pet]:
    pass

@router.get("/pet/{pet_id}", response_model=list[schemas.PetRead])
def get_pet_by_id(pet_id: int, session: SessionDep):
    pass

@router.patch("/pet/{pet_id}", response_model=schemas.PetRead)
def update_pet(pet_id: int, pet: PetUpdate, session: SessionDep):
    pass

@router.delete("/pet/{pet_id}")
def delete_pet(pet_id: int, session: SessionDep):
    pass