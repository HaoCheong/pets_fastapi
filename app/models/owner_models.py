''' Owner Models

Declarative Base: Used for initialising base fields all models will use

Notes:
- Optional Fields that are either optionally included in the input or optionally NULL on ther return

Relationship:
- Pet: One Owner to Many Pets
'''

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.database import Base


class Owner(Base):
    ''' Owner model '''
    __tablename__ = "pet_owner"

    # Owner Fields
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    home_address: Mapped[str] = mapped_column(String)

    # Pet relation (One-to-Many)
    pets: Mapped[list['Pet']] = relationship("Pet", back_populates="owner")
