from sqlmodel import Session

import app.models.owner_models as owner_models
import app.models.pet_models as pet_models


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