from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import app.models.nutrition_plan_models as model
import app.schemas.nutrition_plan_schemas as schemas


def create_nutrition_plan(db: Session, nutrition_plan: schemas.NutritionPlanCreate):
    ''' Creating an new nutrition plan '''
    db_nutrition_plan = model.NutritionPlan(
        name=nutrition_plan.name,
        description=nutrition_plan.description,
        meal=jsonable_encoder(nutrition_plan.meal),
        starting_date=nutrition_plan.starting_date,
    )

    db.add(db_nutrition_plan)
    db.commit()
    db.refresh(db_nutrition_plan)
    return db_nutrition_plan


def get_all_nutrition_plans(db: Session, skip: int = 0, limit: int = 100):
    ''' Get every instance of nutrition plan, using offset pagination '''
    return db.query(model.NutritionPlan).offset(skip).limit(limit).all()


def get_nutrition_plan_by_id(db: Session, nutrition_plan_id: str):
    ''' Get specific instance of nutrition plan based on provided nutrition plan ID '''
    return db.query(model.NutritionPlan).filter(model.NutritionPlan.id == nutrition_plan_id).first()


def update_nutrition_plan_by_id(db: Session, nutrition_plan_id: str, new_nutrition_plan: schemas.NutritionPlanUpdate):
    ''' Update specific fields of specified instance of nutrition plan on provided nutrition plan ID '''
    db_nutrition_plan = db.query(model.NutritionPlan).filter(
        model.NutritionPlan.id == nutrition_plan_id).first()

    # Converts new_nutrition_plan from model.object to dictionary
    update_nutrition_plan = new_nutrition_plan.dict(exclude_unset=True)

    # Loops through dictionary and update db_nutrition_plan
    for key, value in update_nutrition_plan.items():
        setattr(db_nutrition_plan, key, value)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_nutrition_plan)
    db.commit()
    db.refresh(db_nutrition_plan)

    return db_nutrition_plan


def delete_nutrition_plan_by_id(db: Session, nutrition_plan_id: str):
    ''' Delete specified instance of nutrition plan on provided nutrition plan ID '''
    db_nutrition_plan = db.query(model.NutritionPlan).filter(
        model.NutritionPlan.id == nutrition_plan_id).first()

    db.delete(db_nutrition_plan)
    db.commit()
    return {"Success": True}
