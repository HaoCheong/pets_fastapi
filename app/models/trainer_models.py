from datetime import datetime
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

from app.models.pet_models import PetReadNR, PetTrainerAssociation

if TYPE_CHECKING:
    from app.models.pet_models import Pet

class TrainerBase(SQLModel):
    name: str = Field(index=True)
    description: str
    phone_no: str = Field(unique=True)
    email: str = Field(unique=True)
    date_started: datetime
    
class Trainer(TrainerBase, table=True):
    __tablename__ = 'trainer'
    trainer_id: str = Field(unique=True, primary_key=True)
    pets: list["Pet"] = Relationship(back_populates="trainers", link_model=PetTrainerAssociation)

class TrainerReadNR(TrainerBase):
    trainer_id: str
    date_started: datetime

class TrainerReadWR(TrainerReadNR):
    pets: list["PetReadNR"] = []

class TrainerCreate(TrainerBase):
    trainer_id: str
    date_started: datetime
    
class TrainerUpdate(TrainerBase):
    trainer_id: str | None = None
    name: str | None = None
    description: str | None = None
    phone_no: str | None = None
    email: str | None = None