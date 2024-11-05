from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class PetBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)