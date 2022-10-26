from sqlalchemy.orm import Session

from . import models, schemas

# ======== OWNER CRUD ========

def create_owner(db: Session, owner: schemas.OwnerCreate):
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
    return db.query(models.Owner).offset(skip).limit(limit).all()

def get_owner_by_id(db: Session, id:str):
    return db.query(models.Owner).filter(models.Owner.id == id).first()

def update_owner_by_id(db: Session, id: int, new_owner: schemas.OwnerBase):
    db_owner = db.query(models.Owner).filter(models.Owner.id == id).first()

    update_owner = new_owner.dict(exclude_unset=True)

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

def create_pet(db: Session, pet: schemas.PetBase):
    db_pet = models.Pet(
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

def update_pet_by_id(db: Session, id: int, new_pet: schemas.PetBase):
    db_pet = db.query(models.Pet).filter(models.Pet.id == id).first()

    update_pet = new_pet.dict(exclude_unset=True)

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

def create_trainer(db: Session, trainer: schemas.TrainerBase):
    db_trainer = models.Trainer(
        name=trainer.name,
        age=trainer.age,
    )

    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)
    return db_trainer

def get_all_trainers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Trainer).offset(skip).limit(limit).all()

def get_trainer_by_id(db: Session, trainer_id: str):
    return db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()

def update_trainer_by_id(db: Session, trainer_id: str, new_trainer: schemas.TrainerBase):
    db_trainer = db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()

    update_trainer = new_trainer.dict(exclude_unset=True)

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