"""cruds.py (4)

All the functions which directly manipulate the database. Access via main.py

- All data passed here should be valid data (Validation is done in main)
- Follows the standard: Create, Read, Update, Delete, (Assignment optional)

- db.add(): Adds to local database
- db.commit(): Commit changes in local database to actual database
- db.refresh(): Refresh local instances of object

- create_###: Create an instance of the object and add to DB
- get_all_###: Get all instance of object from table in DB
- get_###_by_id: Get specific instance of object from table in DB (via given ID)
- update_###_by_id: Update specific instance of object from table in DB (via given ID)
- delete_###_by_id: Delete specific instance of object from table in DB (via given ID)

- EXTRA: jsonable_encoder converts model.object into actual dictionary (allow for direct manipulation)
"""

from sqlalchemy.orm import Session
import models, schemas

# ======== OWNER CRUD ========

def create_owner(db: Session, owner: schemas.OwnerCreate):
    fake_hashed_password = owner.password + "thisisahash"
    db_owner = models.Owner(
        id=owner.id,
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
    return db.query(models.Owner).offset(skip).limit(limit).all()

def get_owner_by_id(db: Session, id:str):
    return db.query(models.Owner).filter(models.Owner.id == id).first()

def update_owner_by_id(db: Session, id: int, new_owner: schemas.OwnerUpdate):
    db_owner = db.query(models.Owner).filter(models.Owner.id == id).first()

    # Converts new_owner from model.object to dictionary
    update_owner = new_owner.dict(exclude_unset=True)

    # Loops through dictionary and update db_owner
    for key, value in update_owner.items():
        setattr(db_owner, key, value)

    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def delete_owner_by_id(db: Session, id: int):
    db_owner = db.query(models.Owner).filter(models.Owner.id == id).first()

    db.delete(db_owner)
    db.commit()
    return {"Success": True}


# ======== PET CRUD ========

def create_pet(db: Session, pet: schemas.PetCreate):
    db_pet = models.Pet(
        id=pet.id,
        name=pet.name,
        age=pet.age,
    )

    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def get_all_pets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pet).offset(skip).limit(limit).all()

def get_pet_by_id(db: Session, id: int):
    return db.query(models.Pet).filter(models.Pet.id == id).first()

def update_pet_by_id(db: Session, id: int, new_pet: schemas.PetUpdate):
    db_pet = db.query(models.Pet).filter(models.Pet.id == id).first()

    # Converts new_pet from model.object to dictionary
    update_pet = new_pet.dict(exclude_unset=True)

    # Loops through dictionary and update db_pet
    for key, value in update_pet.items():
        setattr(db_pet, key, value)

    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet

def delete_pet_by_id(db: Session, id: int):
    db_pet = db.query(models.Pet).filter(models.Pet.id == id).first()

    db.delete(db_pet)
    db.commit()
    return {"Success": True}

# ========= TRAINER CRUD ========

def create_trainer(db: Session, trainer: schemas.TrainerCreate):
    db_trainer = models.Trainer(
        trainer_id=trainer.trainer_id,
        name=trainer.name,
        phone_no=trainer.phone_no,
        email=trainer.email,
    )

    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer

def get_all_trainers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trainer).offset(skip).limit(limit).all()

def get_trainer_by_id(db: Session, trainer_id: str):
    return db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()

def update_trainer_by_id(db: Session, trainer_id: str, new_trainer: schemas.TrainerUpdate):
    db_trainer = db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()

    # Converts new_trainer from model.object to dictionary
    update_trainer = new_trainer.dict(exclude_unset=True)

    # Loops through dictionary and update db_trainer
    for key, value in update_trainer.items():
        setattr(db_trainer, key, value)

    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer

def delete_trainer_by_id(db: Session, trainer_id: str):
    db_trainer = db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()

    db.delete(db_trainer)
    db.commit()
    return {"Success": True}

# ======== PET OWNER ASSIGNMENT ========

# Assign pet to owner
def assignToOwner(db: Session, pet_id: int, owner_id: int):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    db_owner = db.query(models.Owner).filter(models.Owner.id == owner_id).first()

    # Treat adding relation like adding to pet owner's pets list
    db_owner.pets.append(db_pet)
    db.add(db_owner)
    db.commit()

    return {"Success", True}

# Unassign pet from owner
def unassignFromOwner(db: Session, pet_id: int, owner_id: int):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    db_owner = db.query(models.Owner).filter(models.Owner.id == owner_id).first()

    # Treat removing relation like removing from pet owner's pets list
    db_owner.pets.remove(db_pet)
    db.add(db_owner)
    db.commit()

    return {"Success", True}

# ======== PET TRAINER ASSIGNMENT ========

# Assign pet to trainer
def assignToTrainer(db: Session, pet_id: int, trainer_id: int):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    db_trainer = db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()

    # Treat adding relation like adding to pet trainers's pets list
    # This can be done the other way with adding trainer to pet's trainer list
    db_trainer.pets.append(db_pet)
    db.add(db_trainer)
    db.commit()

    return {"Success", True}

# Unassign pet to trainer
def unassignFromTrainer(db: Session, pet_id: int, trainer_id: int):
    db_pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    db_trainer = db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()

    # Treat removing relation like removing to pet trainers's pets list
    # This can be done the other way with removing trainer to pet's trainer list
    db_trainer.pets.remove(db_pet)
    db.add(db_trainer)
    db.commit()

    return {"Success", True}