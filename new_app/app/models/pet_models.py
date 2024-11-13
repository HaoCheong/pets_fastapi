from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.owner_models import Owner
    from app.models.nutrition_plan_models import NutritionPlan

class PetBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

class Pet(PetBase, table=True):

    __tablename__ = 'pet'

    id: int = Field(default=None, primary_key=True)
    nickname: str

    owner_id: Optional[int] = Field(default=None, foreign_key="owner.id")
    owner: Optional["Owner"] = Relationship(back_populates="pets")

    nutrition_plan_id: Optional[int] = Field(default=None, foreign_key="nutrition_plan.id")
    nutrition_plan: Optional["NutritionPlan"] = Relationship(back_populates="pet")

class PetReadNR(PetBase):
    id: int
    nickname: str

class PetReadWR(PetReadNR):
    
    owner: Optional["OwnerReadNR"] = None
    nutrition_plan: Optional["NutritionPlanReadNR"] = None 

class PetCreate(PetBase):
    nickname: str

class PetUpdate(PetBase):
    name: str | None = None
    age: int | None = None
    nickname: str | None = None

from app.models.owner_models import OwnerReadNR
from app.models.nutrition_plan_models import NutritionPlanReadNR
PetReadWR.model_rebuild()

## https://github.com/fastapi/sqlmodel/discussions/757