from sqlmodel import Field
from datetime import datetime
import app.models.trainer_models as models



class TrainerReadNR(models.TrainerBase):
    trainer_id: str
    date_started: datetime

class TrainerReadWR(TrainerReadNR):
    pass

class TrainerCreate(models.TrainerBase):
    trainer_id: str
    date_started: datetime
    
class TrainerUpdate(models.TrainerBase):
    trainer_id: str | None = None
    name: str | None = None
    description: str | None = None
    phone_no: str | None = None
    email: str | None = None