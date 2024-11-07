from sqlmodel import Field

import app.models.owner_models as models


class OwnerReadNR(models.OwnerBase):
    id: int

class OwnerReadWR(OwnerReadNR):
    from app.schemas.pet_schemas import PetReadNR
    
    pets: list["PetReadNR"] = []

class OwnerCreate(models.OwnerBase):
    password: str

class OwnerUpdate(models.OwnerBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    home_address: str | None = None