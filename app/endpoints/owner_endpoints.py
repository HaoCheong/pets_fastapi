''' Owner Endpoints

Contains all the function that subsequently call the owner CRUD functions (see CRUD files)
Split was done because it allowed for simplified data validation and db calling.
- Endpoints: Takes in and validates input correctness
- CRUD: Focused on the logic of formatting and manipulating data, under the assumption that the provided data was correct

'''

from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.owner_cruds as cruds
import app.models.owner_models as models
from app.database.database import SessionDep

router = APIRouter()

@router.post("/owner/", response_model=models.OwnerReadNR, tags=['Owners'])
def create_owner(owner: models.OwnerCreate, db: SessionDep):
    db_owner = cruds.create_owner(db=db, new_owner=owner)
    return db_owner

@router.get("/owners/", response_model=list[models.OwnerReadNR], tags=['Owners'])
def get_all_owners(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    db_owners = cruds.get_all_owners(db=db, offset=offset, limit=limit)
    return db_owners

@router.get("/owner/{owner_id}", response_model=models.OwnerReadWR, tags=['Owners'])
def get_owner_by_id(owner_id: int, db: SessionDep):
    
    db_owner = cruds.get_owner_by_id(db=db, owner_id=owner_id)
    if db_owner is None:
        raise HTTPException(status_code=400, detail="Owner does not exist")
    
    return db_owner

@router.patch("/owner/{owner_id}", response_model=models.OwnerReadWR, tags=['Owners'])
def update_owner(owner_id: int, new_owner: models.OwnerUpdate, db: SessionDep):

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
