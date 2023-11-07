from typing import List

from app.helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


import app.schemas.owner_schemas as schemas
import app.cruds.owner_cruds as cruds

router = APIRouter()

@router.post("/owner", response_model=schemas.OwnerReadNR, tags=["Owners"])
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    return cruds.create_owner(db=db, owner=owner)


@router.get("/owner", response_model=List[schemas.OwnerReadNR], tags=["Owners"])
def get_all_owners(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_owners = cruds.get_all_owners(db, skip, limit)
    return db_owners


@router.get("/owner/{owner_id}", response_model=schemas.OwnerReadNR, tags=["Owners"])
def get_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return db_owner


@router.patch("/owner/{owner_id}", response_model=schemas.OwnerReadNR, tags=["Owners"])
def update_owner_by_id(owner_id: int, new_owner: schemas.OwnerReadNR, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return cruds.update_owner_by_id(db, id=owner_id, new_owner=new_owner)


@router.delete("/owner/{owner_id}", tags=["Owners"])
def delete_owner_by_id(owner_id: int, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner_id)
    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    return cruds.delete_owner_by_id(db, id=owner_id)