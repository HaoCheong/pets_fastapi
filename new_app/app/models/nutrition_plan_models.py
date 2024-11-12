from datetime import datetime
from typing import Dict

from sqlmodel import Field, SQLModel, JSON, Column

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
    id: int = Field(default=None, primary_key=True)

class NutritionPlanReadNR(NutritionPlanBase):
    id: int
    starting_date: datetime 

class NutritionPlanReadWR(NutritionPlanReadNR):
    pass

class NutritionPlanCreate(NutritionPlanBase):
    starting_date: datetime 

class NutritionPlanUpdate(NutritionPlanBase):
    name: str | None = None
    description: str | None = None
    meal: str | None = None
    starting_date: datetime | None = None
