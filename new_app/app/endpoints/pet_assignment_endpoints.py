from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database.database import get_session

router = APIRouter()

import app.cruds.owner_cruds as owner_cruds
import app.cruds.pet_assignment_cruds as pet_assignment_cruds
import app.cruds.pet_cruds as pet_cruds

# ======== ASSIGNING PETS TO OWNER ========

@router.post("/assignToOwner/{pet_id}/{owner_id}", tags=["Item Assignments"])
def assign_pet_to_owner(pet_id: int, owner_id: int, db: Session = Depends(get_session)):
    db_owner = owner_cruds.get_owner_by_id(db, owner_id=owner_id)
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet already assigned to owner")

    return pet_assignment_cruds.assign_pet_to_owner(db, pet_id=pet_id, owner_id=owner_id)


@router.post("/unassignFromOwner/{pet_id}/{owner_id}", tags=["Item Assignments"])
def unassign_pet_from_owner(pet_id: int, owner_id: int, db: Session = Depends(get_session)):
    db_owner = owner_cruds.get_owner_by_id(db, owner_id=owner_id)
    db_pet = pet_cruds.get_pet_by_id(db, pet_id=pet_id)

    if not db_owner:
        raise HTTPException(status_code=400, detail="Owner does not exist")

    if not db_pet:
        raise HTTPException(status_code=400, detail="Pet does not exist")

    if db_pet not in db_owner.pets:
        raise HTTPException(
            status_code=400, detail="Pet not assigned to owner")

    return pet_assignment_cruds.unassign_pet_from_owner(db, pet_id=pet_id, owner_id=owner_id)
