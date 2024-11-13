from sqlmodel import Session

import app.models.owner_models as owner_models
import app.models.pet_models as pet_models
import app.models.nutrition_plan_models as nutrition_plan_models


def assign_pet_to_owner(db: Session, pet_id: int, owner_id: int):
    ''' Assign instance of pet to an owner. Many to One Relationship '''

    # Getting both instance of Pet and Owner
    db_pet = db.get(pet_models.Pet, pet_id)
    db_owner = db.get(owner_models.Owner, owner_id)

    # Treat adding relation like adding to pet owner's pets list
    db_owner.pets.append(db_pet)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_owner)
    db.commit()

    return {"Success", True}


def unassign_pet_from_owner(db: Session, pet_id: int, owner_id: int):
    ''' Unassign instance of pet to an owner '''

    # Getting both instance of Pet and Owner
    db_pet = db.get(pet_models.Pet, pet_id)
    db_owner = db.get(owner_models.Owner, owner_id)

    # Treat removing relation like removing from pet owner's pets list
    db_owner.pets.remove(db_pet)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_owner)
    db.commit()

    return {"Success", True}


def assign_pet_to_nutrition_plan(db: Session, pet_id: int, nutrition_plan_id: int):
    ''' Assign instance of pet to an nutrition plan. One to One Relationship '''
    # Getting both instance of Pet and Nutrition Plan
    db_pet = db.get(pet_models.Pet, pet_id)
    db_nutrition_plan = db.get(nutrition_plan_models.NutritionPlan, nutrition_plan_id)

    # Establish the relationship
    db_pet.nutrition_plan = db_nutrition_plan

    # Update them on the DB side, and commit transaction to the database
    db.add(db_pet)
    db.commit()
    return {"Success", True}

# Needs review


def unassign_pet_from_nutrition_plan(db: Session, pet_id: int, nutrition_plan_id: int):
    ''' Unassign instance of pet to an nutrition plan '''

    # Getting both instance of Pet and Nutrition Plan
    db_pet = db.get(pet_models.Pet, pet_id)
    db_nutrition_plan = db.get(nutrition_plan_models.NutritionPlan, nutrition_plan_id)

    # Clear their relationship
    db_pet.nutrition_plan = None
    db_nutrition_plan.pet = None

    # Update them on the DB side, and commit transaction to the database
    db.add(db_nutrition_plan)
    db.commit()

    return {"Success", True}