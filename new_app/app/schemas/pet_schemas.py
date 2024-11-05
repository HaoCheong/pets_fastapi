from sqlmodel import Field

import app.models.pet_model as model

class Pet(model.PetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nickname: str

class PetRead(model.PetBase):
    id: int
    nickname: str

class PetCreate(model.PetBase):
    nickname: str

class PetUpdate(model.PetBase):
    name: str | None = None
    age: int | None = None
    nickname: str | None = None
