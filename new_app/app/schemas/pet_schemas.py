from sqlmodel import Field
from typing import Optional, TYPE_CHECKING
import app.models.pet_models as models


if TYPE_CHECKING:
    from app.schemas.owner_schemas import OwnerReadNR

class PetReadNR(models.PetBase):
    id: int
    nickname: str

class PetReadWR(PetReadNR):
    owner: "OwnerReadNR"

class PetCreate(models.PetBase):
    nickname: str

class PetUpdate(models.PetBase):
    name: str | None = None
    age: int | None = None
    nickname: str | None = None
