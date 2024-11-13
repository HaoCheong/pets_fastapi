from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session

import app.endpoints.nutrition_plan_endpoints as nutrition_plan_endpoints
import app.endpoints.owner_endpoints as owner_endpoints
import app.endpoints.pet_assignment_endpoints as pet_assignment_endpoints
import app.endpoints.pet_endpoints as pet_endpoints
import app.endpoints.trainer_endpoints as trainer_endpoints
import app.metadata as metadata
from app.database.database import create_db_and_tables

app = FastAPI(
    openapi_tags=metadata.tags_metadata,
    title=metadata.app_title,
    description=metadata.app_desc,
    version=metadata.app_version
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return { "connection": True }

app.include_router(pet_endpoints.router)
app.include_router(owner_endpoints.router)
app.include_router(trainer_endpoints.router)
app.include_router(nutrition_plan_endpoints.router)

app.include_router(pet_assignment_endpoints.router)