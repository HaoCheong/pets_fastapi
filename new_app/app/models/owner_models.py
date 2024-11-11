from sqlmodel import Field, SQLModel, Relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.pet_models import Pet
    
class OwnerBase(SQLModel):
    
    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    password: str = Field()
    home_address: str = Field()

class Owner(OwnerBase, table=True):

    id: int = Field(default=None, primary_key=True)
    password: str

    pets: list["Pet"] = Relationship(back_populates='owner')
