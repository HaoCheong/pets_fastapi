from typing import List, Union

from pydantic import BaseModel

class OwnerBase(BaseModel):
    id: int
    name: str
    email: str
    home_address: str

    class Config:
        orm_mode = True

class OwnerCreate(OwnerBase):
    password: str


class PetBase(BaseModel):
    id: int
    name: str
    age: int

    class Config:
        orm_mode = True

class TrainerBase(BaseModel):
    trainer_id: str
    name: str
    phone_no: int
    email: str

    class Config:
        orm_mode = True