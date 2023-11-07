# from typing import List, Union, Optional
# from pydantic import BaseModel
# from datetime import datetime

# from owner_schemas import OwnerReadNR
# from trainer_schemas import TrainerReadNR
# from nutrition_plan_schemas import NutritionPlanReadNR

# '''
# ======== BASE SCHEMAS ========
# Schema containing information that will be expected to all other schema
# '''

# class PetBase(BaseModel):
#     ''' Owners Base Schema '''
#     name: str
#     age: int

#     # Allow for Object Relational Mapping (Treating relation like nested objects)
#     class Config:
#         orm_mode = True

# '''
# ======== CREATE SCHEMA ========
# Schema inherit Base schemas, for when new instance of object is created
#  - Used when unknowable data is required
#  - Sometimes used to prevent sensitive data from leaking into the other API.
# '''

# class PetCreate(PetBase):
#     ''' Pet Create Schema, no difference. Kept for potential future expansion '''
#     pass

# '''
# ======== READ NO RELATION ========
# Schema inherit Base schemas, for reading object data WITHOUT relational information
#  - Used in "Get All" cruds to provide reduced network load on large complex data
#  - Used when relationships are represented in the return.
#        - Pets is dependent on the 3 other models, returning all that data for every pet is heavy on the network.
#  - Used when data are self-referential, self referential data could result in a recursive loop as it expands repeatedly
# '''

# class PetReadNR(PetBase):
#     ''' Pet Read w/o relation Schema '''
#     id: int

# '''
# ======== READ WITH RELATION ========
# Schema inherit No Relation schemas, for reading object data WITH relational information
#  - Used when data is specfied and requires pulling all data of its relation
#  - Built off the non-relational read schema
#  - Pulled data uses non-relational read to prevent heavy network load
# '''

# class PetReadWR(PetReadNR):
#     ''' Pet Read w/ relation Schema '''
#     trainers: List[TrainerReadNR]
#     nutrition_plan: Union[NutritionPlanReadNR, None]
#     owner: Union[OwnerReadNR, None]

# '''
# ======== UPDATE SCHEMA ========
# Schema inherit Base schema, for updating existing information
# On update, any optional field not included will not be updated
# Typically a carbon copy of the base field with everything overwritten with the Optional typing
# The "= None" is a default you initialise which allows for you to not require inputting the field in the body of the request
# '''

# class PetUpdate(PetBase):
#     ''' Pet update schema '''
#     name: Optional[str] = None
#     age: Optional[int] = None