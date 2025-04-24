''' Trainer CRUDs

Contains all the base functionailities for reading and writing trainer data into the database
5 base functionality:
- Create
- Read All instance
- Read an instance given an ID
- Update an instance given an ID
- Delete an instance given an ID

'''

from fastapi import HTTPException
from sqlmodel import Session, select

import app.models.trainer_models as models


def create_trainer(db: Session, new_trainer: models.TrainerCreate):
    
    db_trainer = models.Trainer.model_validate(new_trainer)

    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)

    return db_trainer

def get_all_trainers(db: Session, offset: int = 0, limit: int = 100):
    trainer = db.exec(select(models.Trainer).offset(offset).limit(limit)).all()
    return trainer

def get_trainer_by_id(db: Session, trainer_id: str):

    trainer = db.get(models.Trainer, trainer_id)

    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    
    return trainer

def update_trainer_by_id(db: Session, trainer_id: str, new_trainer: models.TrainerUpdate):
    trainer_db = db.get(models.Trainer, trainer_id)
    
    if not trainer_db:
        raise HTTPException(status_code=404, detail="Trainer not found")
    
    trainer_data = new_trainer.model_dump(exclude_unset=True)
    trainer_db.sqlmodel_update(trainer_data)

    db.add(trainer_db)
    db.commit()
    db.refresh(trainer_db)

    return trainer_db

def delete_trainer_by_id(db: Session, trainer_id: str):
    trainer = db.get(models.Trainer, trainer_id)

    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    
    db.delete(trainer)
    db.commit()

    return {"Success": True}
