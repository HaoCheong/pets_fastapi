from datetime import datetime
from typing import Dict, TYPE_CHECKING, List, Optional

from sqlmodel import Field, SQLModel, JSON, Column, Relationship

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
    meal: str | None = None
    starting_date: datetime | None = None

from app.models.pet_models import PetReadNR
NutritionPlanReadWR.model_rebuild()