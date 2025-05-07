'''Nutrition Plan Schemas

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
from typing import Union, Optional, TYPE_CHECKING
from pydantic import BaseModel, ConfigDict
from datetime import datetime

if TYPE_CHECKING:
    from app.schemas.pet_schemas import PetReadNR


class MealBase(BaseModel):
    ''' Meal Base Schema, used for input check in NutritionPlanBase '''
    protein: str
    carb: str
    fibre: str


class NutritionPlanBase(BaseModel):
    ''' Nutrition Plan Base Schema '''
    name: str
    description: str
    meal: MealBase
    starting_date: datetime

    # Allow for Object Relational Mapping (Treating relation like nested objects)
    model_config = ConfigDict(from_attributes=True)


class NutritionPlanCreate(NutritionPlanBase):
    ''' Nutrition Plan Create Schema, no difference. Kept for potential future expansion '''
    pass


class NutritionPlanReadNR(NutritionPlanBase):
    ''' Nutrition Plan Read w/o relation Schema '''
    id: int


class NutritionPlanReadWR(NutritionPlanReadNR):
    ''' Nutrition Plan Read w/ relation Schema '''

    pet: Union["PetReadNR", None]


class NutritionPlanUpdate(NutritionPlanBase):
    ''' Nutrition Plan update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    meal: Optional[MealBase] = None


NutritionPlanReadWR.model_rebuild()
