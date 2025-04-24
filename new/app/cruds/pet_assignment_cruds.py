from sqlalchemy.orm import Session

import app.models.pet_models as pet_models
import app.models.owner_models as owner_models
import app.models.trainer_models as trainer_models
import app.models.nutrition_plan_models as nutrition_plan_models


def assign_pet_to_owner(db: Session, pet_id: int, owner_id: int):
    ''' Assign instance of pet to an owner. Many to One Relationship '''

    # Getting both instance of Pet and Owner
    db_pet = db.query(pet_models.Pet).filter(
        pet_models.Pet.id == pet_id).first()
    db_owner = db.query(owner_models.Owner).filter(
        owner_models.Owner.id == owner_id).first()

    # Treat adding relation like adding to pet owner's pets list
    db_owner.pets.append(db_pet)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_owner)
    db.commit()

    return {"Success", True}


def unassign_pet_from_owner(db: Session, pet_id: int, owner_id: int):
    ''' Unassign instance of pet to an owner '''

    # Getting both instance of Pet and Owner
    db_pet = db.query(pet_models.Pet).filter(
        pet_models.Pet.id == pet_id).first()
    db_owner = db.query(owner_models.Owner).filter(
        owner_models.Owner.id == owner_id).first()

    # Treat removing relation like removing from pet owner's pets list
    db_owner.pets.remove(db_pet)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_owner)
    db.commit()

    return {"Success", True}

# ======== PET TRAINER ASSIGNMENT ================

# Assign pet to trainer


def assign_pet_to_trainer(db: Session, pet_id: int, trainer_id: int):
    ''' Assign instance of pet to an trainer. Many to Many Relationship '''

    # Getting both instance of Pet and Trainer
    db_pet = db.query(pet_models.Pet).filter(
        pet_models.Pet.id == pet_id).first()
    db_trainer = db.query(trainer_models.Trainer).filter(
        trainer_models.Trainer.trainer_id == trainer_id).first()

    # Treat adding relation like adding to pet trainers's pets list
    # This can be done the other way with adding trainer to pet's trainer list
    db_trainer.pets.append(db_pet)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_trainer)
    db.commit()

    return {"Success", True}

# Unassign pet to trainer


def unassign_pet_from_trainer(db: Session, pet_id: int, trainer_id: int):
    ''' Unassign instance of pet to an trainer '''

    # Getting both instance of Pet and Trainer
    db_pet = db.query(pet_models.Pet).filter(
        pet_models.Pet.id == pet_id).first()
    db_trainer = db.query(trainer_models.Trainer).filter(
        trainer_models.Trainer.trainer_id == trainer_id).first()

    # Treat removing relation like removing to pet trainers's pets list
    # This can be done the other way with removing trainer to pet's trainer list
    db_trainer.pets.remove(db_pet)

    # Update them on the DB side, and commit transaction to the database
    db.add(db_trainer)
    db.commit()

    return {"Success", True}

# ======== PET NUTRITIONAL PLAN ASSIGNMENT ================


def assign_pet_to_nutrition_plan(db: Session, pet_id: int, nutrition_plan_id: int):
    ''' Assign instance of pet to an nutrition plan. One to One Relationship '''
    # Getting both instance of Pet and Nutrition Plan
    db_pet = db.query(pet_models.Pet).filter(
        pet_models.Pet.id == pet_id).first()
    db_nutrition_plan = db.query(nutrition_plan_models.NutritionPlan).filter(
        nutrition_plan_models.NutritionPlan.id == nutrition_plan_id).first()

    # Establish the relationship
    db_pet.nutrition_plan = db_nutrition_plan

    # Update them on the DB side, and commit transaction to the database
    db.add(db_pet)
    db.commit()
    return {"Success", True}

# Needs review


def unassign_pet_from_nutrition_plan(db: Session, pet_id: int):
    ''' Unassign instance of pet to an nutrition plan '''

    # Getting both instance of Pet and Nutrition Plan
    db_pet = db.query(pet_models.Pet).filter(
        pet_models.Pet.id == pet_id).first()
    db_nutrition_plan = db.query(nutrition_plan_models.NutritionPlan).filter(
        nutrition_plan_models.NutritionPlan.id == db_pet.nutrition_plan.id).first()

    # Clear their relationship
    db_pet.nutrition_plan = None
    db_nutrition_plan.pet = None

    # Update them on the DB side, and commit transaction to the database
    db.add(db_pet)
    db.add(db_nutrition_plan)
    db.commit()

    return {"Success", True}
