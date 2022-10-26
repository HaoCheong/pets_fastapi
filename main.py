from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import cruds, models, schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/owner", response_model=schemas.OwnerBase)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_owner = cruds.get_owner_by_id(db, id=owner.id)

    if db_owner:
        raise HTTPException(status_code=400, detail="Owner already exist")

    return cruds.create_owner(db=db, owner=owner)