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
    pass
    # pet: Union["PetReadNR", None]


class NutritionPlanUpdate(NutritionPlanBase):
    ''' Nutrition Plan update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    meal: Optional[MealBase] = None


# from app.schemas.pet_schemas import PetReadNR
NutritionPlanReadWR.model_rebuild()
