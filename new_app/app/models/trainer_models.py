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