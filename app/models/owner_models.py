''' Owner Models

Contains both Table Models and Data Models that are used for Owner Operations.
- Base SQLModel: Used for initialising base fields all models will use
- Table Model: Inherited from SQL Model, includes other fields required for all other data models
- Data Models: Inherited from the Table Model or other Data Model. Determines what data is returned from given requests

Notes:
- Optional Fields that are either optionally included in the input or optionally NULL on ther return
- TYPE_CHECKING is to bypass the circular import generated from the required typing in various data models
- Imports at the bottom are for data models imported. Also to bypass circular import

Relationship:
- Pet: One Owner to Many Pets
'''

from typing import TYPE_CHECKING

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
    
    pets: list["PetReadNR"] = []

class OwnerCreate(OwnerBase):
    password: str

class OwnerUpdate(OwnerBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    home_address: str | None = None

from app.models.pet_models import PetReadNR

OwnerReadWR.model_rebuild()
