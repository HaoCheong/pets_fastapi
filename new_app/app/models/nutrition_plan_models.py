from sqlmodel import Field, SQLModel
from datetime import datetime

class NutritionPlanBase(SQLModel):
    
    name: str = Field(index=True)
    description: str
    meal: str
    starting_date: datetime

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
