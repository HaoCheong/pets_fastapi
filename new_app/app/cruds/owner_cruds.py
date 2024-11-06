from fastapi import HTTPException
from sqlmodel import Session, select

import app.schemas.owner_schemas as schemas


def create_owner(db: Session, new_owner: schemas.OwnerCreate):
    
    db_owner = schemas.Owner.model_validate(new_owner)

    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)

    return db_owner

def get_all_owners(db: Session, offset: int = 0, limit: int = 100):
    owner = db.exec(select(schemas.Owner).offset(offset).limit(limit)).all()
    return owner

def get_owner_by_id(db: Session, owner_id: int):

    owner = db.get(schemas.Owner, owner_id)

    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    return owner

def update_owner_by_id(db: Session, owner_id: int, new_owner: schemas.OwnerUpdate):
    owner_db = db.get(schemas.Owner, owner_id)
    
    if not owner_db:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    owner_data = new_owner.model_dump(exclude_unset=True)
    owner_db.sqlmodel_update(owner_data)

    db.add(owner_db)
    db.commit()
    db.refresh(owner_db)

    return owner_db

def delete_owner_by_id(db: Session, owner_id: int):
    owner = db.get(schemas.Owner, owner_id)

    if not owner:
        raise HTTPException(status_code=404, detail="Owner not found")
    
    db.delete(owner)
    db.commit()

    return {"Success": True}
