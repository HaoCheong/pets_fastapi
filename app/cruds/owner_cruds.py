from sqlalchemy.orm import Session
import app.model as models
import app.schemas as schemas
from fastapi.encoders import jsonable_encoder

def create_owner(db: Session, owner: schemas.OwnerCreate):
    ''' Creating an new pet owner '''
    fake_hashed_password = owner.password + "thisisahash"
    db_owner = models.Owner(
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
    return db.query(models.Owner).offset(skip).limit(limit).all()


def get_owner_by_id(db: Session, id: str):
    ''' Get specific instance of owner based on provided owner ID '''
    return db.query(models.Owner).filter(models.Owner.id == id).first()


def update_owner_by_id(db: Session, id: int, new_owner: schemas.OwnerUpdate):
    ''' Update specific fields of specified instance of owner on provided owner ID '''
    db_owner = db.query(models.Owner).filter(models.Owner.id == id).first()

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
    db_owner = db.query(models.Owner).filter(models.Owner.id == id).first()

    db.delete(db_owner)
    db.commit()
    return {"Success": True}