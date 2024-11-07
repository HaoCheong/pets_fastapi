from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.trainer_cruds as cruds
import app.schemas.trainer_schemas as schemas
from app.database.database import SessionDep

router = APIRouter()

@router.post("/trainer/", response_model=schemas.TrainerReadWR, tags=['Trainers'])
def create_trainer(trainer: schemas.TrainerCreate, db: SessionDep):
    db_trainer = cruds.create_trainer(db=db, new_trainer=trainer)
    return db_trainer

@router.get("/trainers/", response_model=list[schemas.TrainerReadNR], tags=['Trainers'])
def get_all_trainers(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    db_trainers = cruds.get_all_trainers(db=db, offset=offset, limit=limit)
    return db_trainers

@router.get("/trainer/{trainer_id}", response_model=schemas.TrainerReadWR, tags=['Trainers'])
def get_trainer_by_id(trainer_id: str, db: SessionDep):
    
    db_trainer = cruds.get_trainer_by_id(db=db, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=400, detail="Trainer does not exist")
    
    return db_trainer

@router.patch("/trainer/{trainer_id}", response_model=schemas.TrainerReadWR, tags=['Trainers'])
def update_trainer(trainer_id: str, new_trainer: schemas.TrainerUpdate, db: SessionDep):

    db_trainer = cruds.get_trainer_by_id(db=db, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=400, detail="Trainer does not exist")
    
    return cruds.update_trainer_by_id(db=db, trainer_id=trainer_id, new_trainer=new_trainer)

@router.delete("/trainer/{trainer_id}", tags=['Trainers'])
def delete_trainer(trainer_id: str, db: SessionDep):
    
    db_trainer = cruds.get_trainer_by_id(db=db, trainer_id=trainer_id)
    if db_trainer is None:
        raise HTTPException(status_code=400, detail="Trainer does not exist")
    
    return cruds.delete_trainer_by_id(db=db, trainer_id=trainer_id)
