from sqlmodel import Field

import app.models.pet_models as models

class Pet(models.PetBase, table=True):
    id: int = Field(default=None, primary_key=True)
    nickname: str

class PetReadNR(models.PetBase):
    id: int
    nickname: str

class PetReadWR(PetReadNR):
    pass

class PetCreate(models.PetBase):
    nickname: str

class PetUpdate(models.PetBase):
    name: str | None = None
    age: int | None = None
    nickname: str | None = None
