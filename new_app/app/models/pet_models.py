from sqlmodel import Field, SQLModel


class PetBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)