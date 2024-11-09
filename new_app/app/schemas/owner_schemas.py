from sqlmodel import Field
from typing import TYPE_CHECKING, Optional, List
import app.models.owner_models as models

if TYPE_CHECKING:
    from app.schemas.pet_schemas import PetReadNR

class OwnerReadNR(models.OwnerBase):
    id: int

class OwnerReadWR(OwnerReadNR):
    pets: Optional[List["PetReadNR"]] = []

class OwnerCreate(models.OwnerBase):
    password: str

class OwnerUpdate(models.OwnerBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    home_address: str | None = None