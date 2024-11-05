from sqlmodel import Field

import app.models.pets_models as models

class Pet(models.PetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nickname: str

class PetRead(models.PetBase):
    id: int

class PetCreate(models.PetBase):
    nickname: str

class PetUpdate(models.PetBase):
    name: str | None = None
    age: int | None = None
    nickname: str | None = None