from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

# import owner_model as models
# import owner_schemas as schemas

# from app.models.owner_model import Owner
# from app.schemas.owner_schemas import OwnerCreate, OwnerUpdate

import app.models.owner_model as model
import app.schemas.owner_schemas as schemas

def create_owner(db: Session, owner: schemas.OwnerCreate):
    ''' Creating an new pet owner '''
    fake_hashed_password = owner.password + "thisisahash"
    db_owner = model.Owner(
        email=owner.email,
        name=owner.name,
        home_address=owner.home_address,
        password=fake_hashed_password
    )

    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


def get_all_owners(db: Session, skip: int = 0, limit: int = 100):
    ''' Get every instance of pet owner, using offset pagination '''
    return db.query(model.Owner).offset(skip).limit(limit).all()


def get_owner_by_id(db: Session, id: str):
    ''' Get specific instance of owner based on provided owner ID '''
    return db.query(model.Owner).filter(model.Owner.id == id).first()


def update_owner_by_id(db: Session, id: int, new_owner: schemas.OwnerUpdate):
    ''' Update specific fields of specified instance of owner on provided owner ID '''
    db_owner = db.query(model.Owner).filter(model.Owner.id == id).first()

    # Converts new_owner from model object to dictionary
    update_owner = new_owner.dict(exclude_unset=True)

    # Loops through dictionary and update db_owner
    for key, value in update_owner.items():
        setattr(db_owner, key, value)

    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner


def delete_owner_by_id(db: Session, id: int):
    ''' Delete specified instance of owner on provided owner ID '''
    db_owner = db.query(model.Owner).filter(model.Owner.id == id).first()

    db.delete(db_owner)
    db.commit()
    return {"Success": True}