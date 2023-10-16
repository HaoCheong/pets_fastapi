"""schemas.py (3)

The expected structure/schema of a input or output value

- For type safety during DB manipulation
- Technically optionally, but necessary for auto-documentation
- Can be thought of as the JSON the database expect to receive and/or return

"""

from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

# ======== BASE SCHEMAS ========
# Schema containing information that will be expected to all other schema

# Owner Base Schema


class OwnerBase(BaseModel):
    name: str
    email: str
    home_address: str

   # Allow for Object Relational Mapping (Treating relation like nested objects)
    class Config:
        orm_mode = True

# Pet Base Schema


class PetBase(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True

# Trainer Base Schema


class TrainerBase(BaseModel):
    name: str
    description: str
    phone_no: str
    email: str
    date_started: datetime

    class Config:
        orm_mode = True

class MealBase(BaseModel):
    protein: str
    carb: str
    fibre: str

class NutritionPlanBase(BaseModel):
    name: str
    description: str
    meal: MealBase
    starting_date: datetime

    class Config:
        orm_mode = True

# ======== CREATE SCHEMA ========
# Schema inherit Base schemas, for when new instance of object is created


class OwnerCreate(OwnerBase):
    password: str  # Password on for creation, means no accidental leak by other schemas


class PetCreate(PetBase):
    pass


class TrainerCreate(TrainerBase):
    trainer_id: str

class NutritionPlanCreate(NutritionPlanBase):
    pass

# ======== READ NO RELATION ========
# Schema inherit Base schemas, for reading object data WITHOUT relational information

class TrainerReadNR(TrainerBase):
    trainer_id: str

class OwnerReadNR(OwnerBase):
    id: int

class NutritionPlanReadNR(NutritionPlanBase):
    id: int

class PetReadNR(PetBase):
    id: int




# ======== READ WITH RELATION ========
# Schema inherit No Relation schemas, for reading object data WITH relational information


class TrainerReadWR(TrainerReadNR):
    pets: List[PetReadNR]


class PetReadWR(PetReadNR):
    # Returns list with schema with NO RELATION to prevent infinite loop for Many-to-Many
    trainers: List[TrainerReadNR]
    nutrition_plan: Union[NutritionPlanReadNR, None]
    owner: Union[OwnerReadNR, None]


class OwnerReadWR(OwnerReadNR):
    # Returns list with schema with NO RELATION to prevent infinite loop for Many-to-Many
    pets: List[PetReadNR]

class NutritionPlanReadWR(NutritionPlanReadNR):
    # Returns list with schema with NO RELATION to prevent infinite loop for Many-to-Many
    pet: Union[PetReadNR, None]

# ======== UPDATE SCHEMA ========
# Schema inherit Base schema, for updating existing information
# On update, any field not included will not be updated


class OwnerUpdate(OwnerBase):
    name: Optional[str]
    email: Optional[str]
    home_address: Optional[str]


class PetUpdate(PetBase):
    name: Optional[str]
    age: Optional[int]


class TrainerUpdate(TrainerBase):

    # Trainer ID in this case is updatable, Pet and Owner cannot update their ID
    trainer_id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    phone_no: Optional[str]
    email: Optional[str]

class NutritionPlanUpdate(NutritionPlanBase):
    name: Optional[str]
    description: Optional[str]
    meal: Optional[MealBase]