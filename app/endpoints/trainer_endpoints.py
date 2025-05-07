from typing import List

from app.helpers import get_db
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

import app.schemas.trainer_schemas as schemas
import app.cruds.trainer_cruds as cruds

router = APIRouter()


@router.post("/api/v1/trainer", response_model=schemas.TrainerReadNR, tags=["Trainers"])
def create_trainer(trainer: schemas.TrainerCreate, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer.trainer_id)
    if db_trainer:
        raise HTTPException(status_code=400, detail="Trainer already exist")

    return cruds.create_trainer(db=db, trainer=trainer)


@router.get("/api/v1/trainers", response_model=List[schemas.TrainerReadNR], tags=["Trainers"])
def get_all_trainers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_trainers = cruds.get_all_trainers(db, skip, limit)
    return db_trainers


@router.get("/api/v1/trainer/{trainer_id}", response_model=schemas.TrainerReadWR, tags=["Trainers"])
def get_trainer_by_id(trainer_id: str, db: Session = Depends(get_db)):
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return db_trainer


@router.patch("/api/v1/trainer/{trainer_id}", response_model=schemas.TrainerReadNR, tags=["Trainers"])
def update_trainer_by_id(trainer_id: str, new_trainer: schemas.TrainerUpdate, db: Session = Depends(get_db)):

    # Existance check for trainer prior to update
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return cruds.update_trainer_by_id(db, trainer_id=trainer_id, new_trainer=new_trainer)


@router.delete("/api/v1/trainer/{trainer_id}", tags=["Trainers"])
def delete_trainer_by_id(trainer_id: str, db: Session = Depends(get_db)):

    # Existance check for trainer prior to delete
    db_trainer = cruds.get_trainer_by_id(db, trainer_id=trainer_id)
    if not db_trainer:
        raise HTTPException(status_code=400, detail="Trainer does not exist")

    return cruds.delete_trainer_by_id(db, trainer_id=trainer_id)
