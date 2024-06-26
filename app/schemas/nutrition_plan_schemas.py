from typing import Union, Optional
from pydantic import BaseModel
from datetime import datetime

'''
======== BASE SCHEMAS ========
Schema containing information that will be expected to all other schema
'''

class MealBase(BaseModel):
    ''' Meal Base Schema, used for input check in NutritionPlanBase '''
    protein: str
    carb: str
    fibre: str

class NutritionPlanBase(BaseModel):
    ''' Nutrition Plan Base Schema '''
    name: str
    description: str
    meal: MealBase
    starting_date: datetime

    # Allow for Object Relational Mapping (Treating relation like nested objects)
    class Config:
        orm_mode = True

'''
======== CREATE SCHEMA ========
Schema inherit Base schemas, for when new instance of object is created
 - Used when unknowable data is required
 - Sometimes used to prevent sensitive data from leaking into the other API.
'''

class NutritionPlanCreate(NutritionPlanBase):
    ''' Nutrition Plan Create Schema, no difference. Kept for potential future expansion '''
    pass

'''
======== READ NO RELATION ========
Schema inherit Base schemas, for reading object data WITHOUT relational information
 - Used in "Get All" cruds to provide reduced network load on large complex data
 - Used when relationships are represented in the return.
       - Pets is dependent on the 3 other models, returning all that data for every pet is heavy on the network.
 - Used when data are self-referential, self referential data could result in a recursive loop as it expands repeatedly
'''

class NutritionPlanReadNR(NutritionPlanBase):
    ''' Nutrition Plan Read w/o relation Schema '''
    id: int

'''
======== READ WITH RELATION ========
Schema inherit No Relation schemas, for reading object data WITH relational information
 - Used when data is specfied and requires pulling all data of its relation
 - Built off the non-relational read schema
 - Pulled data uses non-relational read to prevent heavy network load
'''

class NutritionPlanReadWR(NutritionPlanReadNR):
    ''' Nutrition Plan Read w/ relation Schema '''
    from app.schemas.pet_schemas import PetReadNR
    pet: Union[PetReadNR, None]

'''
======== UPDATE SCHEMA ========
Schema inherit Base schema, for updating existing information
On update, any optional field not included will not be updated
Typically a carbon copy of the base field with everything overwritten with the Optional typing
The "= None" is a default you initialise which allows for you to not require inputting the field in the body of the request
'''

class NutritionPlanUpdate(NutritionPlanBase):
    ''' Nutrition Plan update schema '''
    name: Optional[str] = None
    description: Optional[str] = None
    meal: Optional[MealBase] = None
