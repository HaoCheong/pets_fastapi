from typing import List, Optional, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from app.schemas.pet_schemas import PetReadNR


class OwnerBase(BaseModel):
    ''' Owners Base Schema '''
    name: str
    email: str
    home_address: str

   # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class OwnerCreate(OwnerBase):
    ''' Owner Create Schema '''
    password: str  # Password on for creation, means no accidental leak by other schemas


class OwnerReadNR(OwnerBase):
    ''' Owner Read w/o relation Schema '''
    id: int


class OwnerReadWR(OwnerReadNR):

    ''' Owner Read w/ relation Schema '''
    pets: List["PetReadNR"]


class OwnerUpdate(OwnerBase):
    ''' Owner update schema '''
    name: Optional[str] = None
    email: Optional[str] = None
    home_address: Optional[str] = None

from app.schemas.pet_schemas import PetReadNR
OwnerReadWR.model_rebuild()
