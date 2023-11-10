from typing import List

from app.helpers import get_db
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import app.schemas.nutrition_plan_schemas as schemas
import app.cruds.nutrition_plan_cruds as cruds

router = APIRouter()

@router.post("/nutrition_plan", response_model=schemas.NutritionPlanReadNR, tags=["Nutrition Plans"])
def create_nutrition_plan(nutrition_plan: schemas.NutritionPlanCreate, db: Session = Depends(get_db)):
    return cruds.create_nutrition_plan(db=db, nutrition_plan=nutrition_plan)


@router.get("/nutrition_plans", response_model=List[schemas.NutritionPlanReadNR], tags=["Nutrition Plans"])
def get_all_nutrition_plans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    db_nutrition_plans = cruds.get_all_nutrition_plans(db, skip, limit)
    return db_nutrition_plans


@router.get("/nutrition_plan/{nutrition_plan_id}", response_model=schemas.NutritionPlanReadWR, tags=["Nutrition Plans"])
def get_nutrition_plan_by_id(nutrition_plan_id: str, db: Session = Depends(get_db)):
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)
    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="Nutrition plan does not exist")

    return db_nutrition_plan


@router.patch("/nutrition_plan/{nutrition_plan_id}", response_model=schemas.NutritionPlanReadWR, tags=["Nutrition Plans"])
def update_nutrition_plan_by_id(nutrition_plan_id: str, new_nutrition_plan: schemas.NutritionPlanUpdate, db: Session = Depends(get_db)):
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)
    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="Nutrition plan does not exist")

    return cruds.update_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id, new_nutrition_plan=new_nutrition_plan)


@router.delete("/nutrition_plan/{nutrition_plan_id}", tags=["Nutrition Plans"])
def delete_nutrition_plan_by_id(nutrition_plan_id: str, db: Session = Depends(get_db)):
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)
    if not db_nutrition_plan:
        raise HTTPException(status_code=400, detail="nutrition_plan does not exist")

    return cruds.delete_nutrition_plan_by_id(db, nutrition_plan_id=nutrition_plan_id)
