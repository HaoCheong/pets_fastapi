from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session

import app.endpoints.pets_endpoints as pets_endpoints

app = FastAPI()

@app.get("/")
def root():
    return { "connection": True }

app.include_router(pets_endpoints.router)
