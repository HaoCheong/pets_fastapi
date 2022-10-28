"""schemas.py (3)

The expected structure/schema of a input or output value

- For type safety during DB manipulation
- Technically optionally, but necessary for auto-documentation
- Can be thought of as the JSON the database expect to receive and/or return

"""

from typing import List, Union, Optional
from pydantic import BaseModel

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
    phone_no: int
    email: str

    class Config:
        orm_mode = True

# ======== CREATE SCHEMA ========
# Schema inherit Base schemas, for when new instance of object is created

class OwnerCreate(OwnerBase):
    id: int
    password: str # Password on for creation, means no accidental leak by other schemas

class PetCreate(PetBase):
    id: int

class TrainerCreate(TrainerBase):
    trainer_id: str

# ======== READ NO RELATION ========
# Schema inherit Base schemas, for reading object data WITHOUT relational information

class TrainerReadNR(TrainerBase):
    trainer_id: str

class PetReadNR(PetBase):
    id: int
    owner_id: Optional[int]

class OwnerReadNR(OwnerBase):
    id: int

# ======== READ WITH RELATION ========
# Schema inherit No Relation schemas, for reading object data WITH relational information

class TrainerReadWR(TrainerReadNR):
    pets: List[PetReadNR]

class PetReadWR(PetReadNR):
    # Returns list with schema with NO RELATION to prevent infinite loop for Many-to-Many
    trainers: List[TrainerReadNR]

class OwnerReadWR(OwnerReadNR):
    # Returns list with schema with NO RELATION to prevent infinite loop for Many-to-Many
    pets: List[PetReadNR]

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

    #Trainer ID in this case is updatable, Pet and Owner cannot update their ID
    trainer_id: Optional[str]
    name: Optional[str]
    phone_no: Optional[int]
    email: Optional[str]