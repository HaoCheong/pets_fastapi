from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session

import app.endpoints.pet_endpoints as pet_endpoints
import app.metadata as metadata

app = FastAPI(
    openapi_tags=metadata.tags_metadata,
    title=metadata.app_title,
    description=metadata.app_desc,
    version=metadata.app_version
)

@app.get("/")
def root():
    return { "connection": True }

app.include_router(pet_endpoints.router)