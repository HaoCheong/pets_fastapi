''' Owner CRUDs

Contains all the base functionailities for reading and writing owner data into the database
5 base functionality:
- Create
- Read All instance
- Read an instance given an ID
- Update an instance given an ID
- Delete an instance given an ID

'''

from fastapi import HTTPException
from sqlmodel import Session, select

import app.models.owner_models as models


def create_owner(db: Session, new_owner: models.OwnerCreate):
    
    db_owner = models.Owner.model_validate(new_owner)

    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)

    return db_owner

def get_all_owners(db: Session, offset: int = 0, limit: int = 100):
    owner = db.exec(select(models.Owner).offset(offset).limit(limit)).all()
    return owner

def get_owner_by_id(db: Session, owner_id: int):

    owner = db.get(models.Owner, owner_id)

    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    return owner

def update_owner_by_id(db: Session, owner_id: int, new_owner: models.OwnerUpdate):
    owner_db = db.get(models.Owner, owner_id)
    
    if not owner_db:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    owner_data = new_owner.model_dump(exclude_unset=True)
    owner_db.sqlmodel_update(owner_data)

    db.add(owner_db)
    db.commit()
    db.refresh(owner_db)

    return owner_db

def delete_owner_by_id(db: Session, owner_id: int):
    owner = db.get(models.Owner, owner_id)

    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    db.delete(owner)
    db.commit()

    return {"Success": True}
