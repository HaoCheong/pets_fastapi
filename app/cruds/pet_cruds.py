''' Pet CRUDs

Contains all the base functionailities for reading and writing pet data into the database
5 base functionality:
- Create
- Read All instance
- Read an instance given an ID
- Update an instance given an ID
- Delete an instance given an ID

'''


from fastapi import HTTPException
from sqlmodel import Session, select

import app.models.pet_models as models


def create_pet(db: Session, new_pet: models.PetCreate):
    
    db_pet = models.Pet.model_validate(new_pet)

    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)

    return db_pet

def get_all_pets(db: Session, offset: int = 0, limit: int = 100):
    db_pet = db.exec(select(models.Pet).offset(offset).limit(limit)).all()
    return db_pet

def get_pet_by_id(db: Session, pet_id: int):

    db_pet = db.get(models.Pet, pet_id)

    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    return db_pet

def update_pet_by_id(db: Session, pet_id: int, new_pet: models.PetUpdate):
    db_pet = db.get(models.Pet, pet_id)
    
    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    pet_data = new_pet.model_dump(exclude_unset=True)
    db_pet.sqlmodel_update(pet_data)

    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)

    return db_pet

def delete_pet_by_id(db: Session, pet_id: int):
    db_pet = db.get(models.Pet, pet_id)

    if not db_pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    db.delete(db_pet)
    db.commit()

    return {"Success": True}
