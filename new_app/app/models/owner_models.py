from typing import TYPE_CHECKING, List, Optional
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.pet_models import Pet, PetReadNR

class OwnerBase(SQLModel):
    
    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    password: str = Field()
    home_address: str = Field()

class Owner(OwnerBase, table=True):

    __tablename__ = 'owner'

    id: int = Field(default=None, primary_key=True)
    password: str

    pets: list["Pet"] = Relationship(back_populates='owner')

class OwnerReadNR(OwnerBase):
    id: int

class OwnerReadWR(OwnerReadNR):
    
    pets: List["PetReadNR"] = []

class OwnerCreate(OwnerBase):
    password: str

class OwnerUpdate(OwnerBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    home_address: str | None = None

from app.models.pet_models import PetReadNR
OwnerReadWR.model_rebuild()