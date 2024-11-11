from sqlmodel import Field, SQLModel
from datetime import datetime

class TrainerBase(SQLModel):
    name: str = Field(index=True)
    description: str
    phone_no: str = Field(unique=True)
    email: str = Field(unique=True)
    date_started: datetime
    
class Trainer(TrainerBase, table=True):
    trainer_id: str = Field(unique=True, primary_key=True)

class TrainerReadNR(TrainerBase):
    trainer_id: str
    date_started: datetime

class TrainerReadWR(TrainerReadNR):
    pass

class TrainerCreate(TrainerBase):
    trainer_id: str
    date_started: datetime
    
class TrainerUpdate(TrainerBase):
    trainer_id: str | None = None
    name: str | None = None
    description: str | None = None
    phone_no: str | None = None
    email: str | None = None