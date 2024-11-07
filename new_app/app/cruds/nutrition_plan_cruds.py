from fastapi import HTTPException
from sqlmodel import Session, select

import app.models.nutrition_plan_models as models
import app.schemas.nutrition_plan_schemas as schemas


def create_nutrition_plan(db: Session, new_nutrition_plan: schemas.NutritionPlanCreate):
    
    db_nutrition_plan = models.NutritionPlan.model_validate(new_nutrition_plan)

    db.add(db_nutrition_plan)
    db.commit()
    db.refresh(db_nutrition_plan)

    return db_nutrition_plan

def get_all_nutrition_plans(db: Session, offset: int = 0, limit: int = 100):
    nutrition_plan = db.exec(select(models.NutritionPlan).offset(offset).limit(limit)).all()
    return nutrition_plan

def get_nutrition_plan_by_id(db: Session, nutrition_plan_id: int):

    nutrition_plan = db.get(models.NutritionPlan, nutrition_plan_id)

    if not nutrition_plan:
        raise HTTPException(status_code=404, detail="NutritionPlan not found")
    
    return nutrition_plan

def update_nutrition_plan_by_id(db: Session, nutrition_plan_id: int, new_nutrition_plan: schemas.NutritionPlanUpdate):
    nutrition_plan_db = db.get(models.NutritionPlan, nutrition_plan_id)
    
    if not nutrition_plan_db:
        raise HTTPException(status_code=404, detail="NutritionPlan not found")
    
    nutrition_plan_data = new_nutrition_plan.model_dump(exclude_unset=True)
    nutrition_plan_db.sqlmodel_update(nutrition_plan_data)

    db.add(nutrition_plan_db)
    db.commit()
    db.refresh(nutrition_plan_db)

    return nutrition_plan_db

def delete_nutrition_plan_by_id(db: Session, nutrition_plan_id: int):
    nutrition_plan = db.get(models.NutritionPlan, nutrition_plan_id)

    if not nutrition_plan:
        raise HTTPException(status_code=404, detail="NutritionPlan not found")
    
    db.delete(nutrition_plan)
    db.commit()

    return {"Success": True}
