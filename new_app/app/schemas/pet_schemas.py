from sqlmodel import Field
from typing import Optional
import app.models.pet_models as models

class PetReadNR(models.PetBase):
    id: int
    nickname: str

class PetReadWR(PetReadNR):
    from app.schemas.owner_schemas import OwnerReadNR
    owner: Optional[OwnerReadNR] = None

class PetCreate(models.PetBase):
    nickname: str

class PetUpdate(models.PetBase):
    name: str | None = None
    age: int | None = None
    nickname: str | None = None
