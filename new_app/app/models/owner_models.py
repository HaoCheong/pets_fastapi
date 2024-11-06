from sqlmodel import Field, SQLModel

class OwnerBase(SQLModel):
    
    name: str = Field(index=True)
    email: str = Field(index=True, unique=True)
    password: str = Field()
    home_address: str = Field()