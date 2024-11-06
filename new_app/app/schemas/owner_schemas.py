from sqlmodel import Field

import app.models.owner_models as models

class Owner(models.OwnerBase, table=True):
    id: int = Field(default=None, primary_key=True)
    password: str

class OwnerReadNR(models.OwnerBase):
    id: int

class OwnerReadWR(OwnerReadNR):
    pass

class OwnerCreate(models.OwnerBase):
    password: str

class OwnerUpdate(models.OwnerBase):
    name: str | None = None
    email: str | None = None
    password: str | None = None
    home_address: str | None = None