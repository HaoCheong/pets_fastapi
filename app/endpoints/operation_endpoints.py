from typing import List

import pandas as pd
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

import app.cruds.pet_cruds as pet_cruds
import app.schemas.pet_schemas as pet_schemas
from app.helpers import get_db

router = APIRouter()


@router.get("/export/pets", tags=["Operations"])
def export_pets(limit: int = 100, db: Session = Depends(get_db)):
    db_pets = pet_cruds.get_all_pets(db=db, limit=limit)
    pets = [pet_schemas.PetReadNR.model_validate(
        pet).__dict__ for pet in db_pets]

    pets_df = pd.DataFrame(pets)
    pets_df.to_csv("/app/pets.csv", sep="|")

    return FileResponse("/app/pets.csv", filename="exported_pets.csv")
