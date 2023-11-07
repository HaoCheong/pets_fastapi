from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

# from pet_schemas import PetReadNR

'''
======== BASE SCHEMAS ========
Schema containing information that will be expected to all other schema
'''

class OwnerBase(BaseModel):
    ''' Owners Base Schema '''
    name: str
    email: str
    home_address: str

   # Allow for Object Relational Mapping (Treating relation like nested objects)
    class Config:
        orm_mode = True

'''
======== CREATE SCHEMA ========
Schema inherit Base schemas, for when new instance of object is created
 - Used when unknowable data is required
 - Sometimes used to prevent sensitive data from leaking into the other API.
'''

class OwnerCreate(OwnerBase):
    ''' Owner Create Schema '''
    password: str  # Password on for creation, means no accidental leak by other schemas

'''
======== READ NO RELATION ========
Schema inherit Base schemas, for reading object data WITHOUT relational information
 - Used in "Get All" cruds to provide reduced network load on large complex data
 - Used when relationships are represented in the return.
       - Pets is dependent on the 3 other models, returning all that data for every pet is heavy on the network.
 - Used when data are self-referential, self referential data could result in a recursive loop as it expands repeatedly
'''

class OwnerReadNR(OwnerBase):
    ''' Owner Read w/o relation Schema '''
    id: int

'''
======== READ WITH RELATION ========
Schema inherit No Relation schemas, for reading object data WITH relational information
 - Used when data is specfied and requires pulling all data of its relation
 - Built off the non-relational read schema
 - Pulled data uses non-relational read to prevent heavy network load
'''

class OwnerReadWR(OwnerReadNR):
    ''' Owner Read w/ relation Schema '''
    # pets: List[PetReadNR]
    pass

'''
======== UPDATE SCHEMA ========
Schema inherit Base schema, for updating existing information
On update, any optional field not included will not be updated
Typically a carbon copy of the base field with everything overwritten with the Optional typing
The "= None" is a default you initialise which allows for you to not require inputting the field in the body of the request
'''

class OwnerUpdate(OwnerBase):
    ''' Owner update schema '''
    name: Optional[str] = None
    email: Optional[str] = None
    home_address: Optional[str] = None