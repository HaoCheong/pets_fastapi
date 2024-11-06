from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.owner_cruds as cruds
import app.schemas.owner_schemas as schemas
from app.database.database import SessionDep

router = APIRouter()

@router.post("/owner/", response_model=schemas.OwnerReadWR, tags=['Owners'])
def create_owner(owner: schemas.OwnerCreate, db: SessionDep):
    db_owner = cruds.create_owner(db=db, new_owner=owner)
    return db_owner

@router.get("/owners/", response_model=list[schemas.OwnerReadNR], tags=['Owners'])
def get_all_owners(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[schemas.Owner]:
    db_owners = cruds.get_all_owners(db=db, offset=offset, limit=limit)
    return db_owners

@router.get("/owner/{owner_id}", response_model=schemas.OwnerReadWR, tags=['Owners'])
def get_owner_by_id(owner_id: int, db: SessionDep):
    
    db_owner = cruds.get_owner_by_id(db=db, owner_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=400, detail="Owner does not exist")
    
    return db_owner

@router.patch("/owner/{owner_id}", response_model=schemas.OwnerReadWR, tags=['Owners'])
def update_owner(owner_id: int, new_owner: schemas.OwnerUpdate, db: SessionDep):

    db_owner = cruds.get_owner_by_id(db=db, owner_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=400, detail="Owner does not exist")
    
    return cruds.update_owner_by_id(db=db, owner_id=owner_id, new_owner=new_owner)

@router.delete("/owner/{owner_id}", tags=['Owners'])
def delete_owner(owner_id: int, db: SessionDep):
    
    db_owner = cruds.get_owner_by_id(db=db, owner_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=400, detail="Owner does not exist")
    
    return cruds.delete_owner_by_id(db=db, owner_id=owner_id)
