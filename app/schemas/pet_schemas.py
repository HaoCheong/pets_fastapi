'''Pet Schemas

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

from app.schemas.nutrition_plan_schemas import NutritionPlanReadNR
from app.schemas.trainer_schemas import TrainerReadNR
from app.schemas.owner_schemas import OwnerReadNR
from typing import List, Union, Optional, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict


if TYPE_CHECKING:
    from app.schemas.owner_schemas import OwnerReadNR
    from app.schemas.trainer_schemas import TrainerReadNR
    from app.schemas.nutrition_plan_schemas import NutritionPlanReadNR


class PetBase(BaseModel):
    ''' Owners Base Schema '''
    name: str
    age: int

    # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class PetCreate(PetBase):
    ''' Pet Create Schema, no difference. Kept for potential future expansion '''
    pass


class PetReadNR(PetBase):
    ''' Pet Read w/o relation Schema '''
    id: int


class PetReadWR(PetReadNR):

    trainers: List["TrainerReadNR"]
    nutrition_plan: Union["NutritionPlanReadNR", None]
    owner: Union["OwnerReadNR", None]


class PetUpdate(PetBase):
    ''' Pet update schema '''
    name: Optional[str] = None


PetReadWR.model_rebuild()
