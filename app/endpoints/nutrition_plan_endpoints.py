from typing import Annotated

from fastapi import APIRouter, HTTPException, Query

import app.cruds.nutrition_plan_cruds as cruds
import app.models.nutrition_plan_models as models
from app.database.database import SessionDep

router = APIRouter()

@router.post("/nutrition_plan/", response_model=models.NutritionPlanReadNR, tags=['Nutrition Plans'])
def create_nutrition_plan(nutrition_plan: models.NutritionPlanCreate, db: SessionDep):
    db_nutrition_plan = cruds.create_nutrition_plan(db=db, new_nutrition_plan=nutrition_plan)
    return db_nutrition_plan

@router.get("/nutrition_plans/", response_model=list[models.NutritionPlanReadNR], tags=['Nutrition Plans'])
def get_all_nutrition_plans(db: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    db_nutrition_plans = cruds.get_all_nutrition_plans(db=db, offset=offset, limit=limit)
    return db_nutrition_plans

@router.get("/nutrition_plan/{nutrition_plan_id}", response_model=models.NutritionPlanReadWR, tags=['Nutrition Plans'])
def get_nutrition_plan_by_id(nutrition_plan_id: int, db: SessionDep):
    
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db=db, nutrition_plan_id=nutrition_plan_id)
    if db_nutrition_plan is None:
        raise HTTPException(status_code=400, detail="NutritionPlan does not exist")
    
    return db_nutrition_plan

@router.patch("/nutrition_plan/{nutrition_plan_id}", response_model=models.NutritionPlanReadWR, tags=['Nutrition Plans'])
def update_nutrition_plan(nutrition_plan_id: int, new_nutrition_plan: models.NutritionPlanUpdate, db: SessionDep):

    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db=db, nutrition_plan_id=nutrition_plan_id)
    if db_nutrition_plan is None:
        raise HTTPException(status_code=400, detail="NutritionPlan does not exist")
    
    return cruds.update_nutrition_plan_by_id(db=db, nutrition_plan_id=nutrition_plan_id, new_nutrition_plan=new_nutrition_plan)

@router.delete("/nutrition_plan/{nutrition_plan_id}", tags=['Nutrition Plans'])
def delete_nutrition_plan(nutrition_plan_id: int, db: SessionDep):
    
    db_nutrition_plan = cruds.get_nutrition_plan_by_id(db=db, nutrition_plan_id=nutrition_plan_id)
    if db_nutrition_plan is None:
        raise HTTPException(status_code=400, detail="NutritionPlan does not exist")
    
    return cruds.delete_nutrition_plan_by_id(db=db, nutrition_plan_id=nutrition_plan_id)
