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

    pass
    # trainers: List["TrainerReadNR"]
    # nutrition_plan: Union["NutritionPlanReadNR", None]
    # owner: Union["OwnerReadNR", None]


class PetUpdate(PetBase):
    ''' Pet update schema '''
    name: Optional[str] = None


# from app.schemas.owner_schemas import OwnerReadNR
# from app.schemas.trainer_schemas import TrainerReadNR
# from app.schemas.nutrition_plan_schemas import NutritionPlanReadNR
PetReadWR.model_rebuild()
