''' Nutrition Plan Models

Contains both Table Models and Data Models that are used for Nutrition Plan Operations.
- Base SQLModel: Used for initialising base fields all models will use
- Table Model: Inherited from SQL Model, includes other fields required for all other data models
- Data Models: Inherited from the Table Model or other Data Model. Determines what data is returned from given requests

Notes:
- Optional Fields that are either optionally included in the input or optionally NULL on ther return
- TYPE_CHECKING is to bypass the circular import generated from the required typing in various data models
- Imports at the bottom are for data models imported. Also to bypass circular import

Relationship:
- Nutrition Plan: One Nutrition Plan to One Pet 
'''

from datetime import datetime
from typing import TYPE_CHECKING, Dict, List, Optional

from sqlmodel import JSON, Column, Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.pet_models import Pet


class MealBase(SQLModel):
    ''' Meal Base Schema, used for input check in NutritionPlanBase '''
    protein: str
    carb: str
    fibre: str

class NutritionPlanBase(SQLModel):
    
    name: str = Field(index=True)
    description: str
    meal: Dict = Field(default_factory=MealBase, sa_column=Column(JSON))
    starting_date: datetime

    class Config:
        arbitrary_types_allowed = True

class NutritionPlan(NutritionPlanBase, table=True):
    __tablename__ = 'nutrition_plan'

    id: int = Field(default=None, primary_key=True)
    pet: "Pet" = Relationship(back_populates='nutrition_plan', sa_relationship_kwargs={"uselist": False})

class NutritionPlanReadNR(NutritionPlanBase):
    id: int
    starting_date: datetime 

class NutritionPlanReadWR(NutritionPlanReadNR):
    pet: Optional["PetReadNR"] = None

class NutritionPlanCreate(NutritionPlanBase):
    starting_date: datetime 

class NutritionPlanUpdate(NutritionPlanBase):
    name: str | None = None
    description: str | None = None
    meal: Dict | None = None
    starting_date: datetime | None = None

from app.models.pet_models import PetReadNR

NutritionPlanReadWR.model_rebuild()
