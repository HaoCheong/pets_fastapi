'''Owner Schemas

Contains the pydantic structures used to enforce the typing and return values during operation

Schema Types:
- Base Schema: Acts as the starting base containing all the fields that are shared with all remaining schema
- Create Schema: Inherited from Base, contains any new information that is unique to the input during creation
- ReadNR Schema: Inherited from Base, contains all the information that is to be read. Does not include any relation data from other linked tables
- ReadWR Schema: Inherited from ReadNR, includes relation data from other linked table
- Update Schema: Inherited from Base, includes all the fields that can be updated, "None" defaults means you do strictly have to include those fields in the body.

Notes:
- TYPE_CHECKING check for the imports are to allow for IDE checking
- Imports of the shared models and the model rebuild is to avoid circular import
'''

from app.schemas.pet_schemas import PetReadNR
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


OwnerReadWR.model_rebuild()
