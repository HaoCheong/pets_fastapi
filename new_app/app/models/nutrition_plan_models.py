from sqlmodel import Field, SQLModel
from datetime import datetime

class NutritionPlanBase(SQLModel):
    
    name: str = Field(index=True)
    description: str
    meal: str
    starting_date: datetime