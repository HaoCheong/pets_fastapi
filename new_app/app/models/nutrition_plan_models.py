from sqlmodel import Field, SQLModel
from datetime import datetime

class NutritionPlanBase(SQLModel):
    
    name: str = Field(index=True)
    description: str
    meal: str
    starting_date: datetime

class NutritionPlan(NutritionPlanBase, table=True):
    id: int = Field(default=None, primary_key=True)