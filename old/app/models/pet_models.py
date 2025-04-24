''' Pet Models

Contains both Table Models and Data Models that are used for Pet Operations.
- Base SQLModel: Used for initialising base fields all models will use
- Table Model: Inherited from SQL Model, includes other fields required for all other data models
- Data Models: Inherited from the Table Model or other Data Model. Determines what data is returned from given requests

Notes:
- Optional Fields that are either optionally included in the input or optionally NULL on ther return
- TYPE_CHECKING is to bypass the circular import generated from the required typing in various data models
- Imports at the bottom are for data models imported. Also to bypass circular import

Relationship:
- Owner: Many Pets To One Owner
- Trainer: Many Pets to Many Trainers
- Nutrition Plan: One Pet to One Nutrition Plan
'''

from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.nutrition_plan_models import NutritionPlan
    from app.models.owner_models import Owner
    from app.models.trainer_models import Trainer

class PetTrainerAssociation(SQLModel, table=True):
    '''
    Pet to Trainer Many to Many Association Object
    '''

    __tablename__ = 'pet_trainer_association'
    pet_id: int | None = Field(default=None, foreign_key="pet.id", primary_key=True)
    trainer_id: str | None = Field(default=None, foreign_key="trainer.trainer_id", primary_key=True)

class PetBase(SQLModel):
    '''
    Pet Base SQL Model
    '''

    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

class Pet(PetBase, table=True):
    '''
    Pet Table Model
    '''

    __tablename__ = 'pet'

    id: int = Field(default=None, primary_key=True)
    nickname: str

    owner_id: Optional[int] = Field(default=None, foreign_key="owner.id")
    owner: Optional["Owner"] = Relationship(back_populates="pets")

    nutrition_plan_id: Optional[int] = Field(default=None, foreign_key="nutrition_plan.id")
    nutrition_plan: Optional["NutritionPlan"] = Relationship(back_populates="pet")

    trainers: list["Trainer"] = Relationship(back_populates="pets", link_model=PetTrainerAssociation)

class PetReadNR(PetBase):
    '''
    Pet Read (No Relation) Data Model - For returning WITHOUT Relationship
    '''

    id: int
    nickname: str

class PetReadWR(PetReadNR):
    '''
    Pet Read (With Relation) Data Model - For returning WITH Relationship
    '''
    
    owner: Optional["OwnerReadNR"] = None
    nutrition_plan: Optional["NutritionPlanReadNR"] = None 
    trainers: Optional[list["TrainerReadNR"]] = None

class PetCreate(PetBase):
    '''
    Pet Create Data Model - For validating input format when creating
    '''

    nickname: str

class PetUpdate(PetBase):
    '''
    Pet Update Data Model - For validating input format when updating
    '''

    name: str | None = None
    age: int | None = None
    nickname: str | None = None

from app.models.nutrition_plan_models import NutritionPlanReadNR
from app.models.owner_models import OwnerReadNR
from app.models.trainer_models import TrainerReadNR

PetReadWR.model_rebuild()

## https://github.com/fastapi/sqlmodel/discussions/757