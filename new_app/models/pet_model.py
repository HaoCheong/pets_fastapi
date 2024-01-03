from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import String

from new_app.database import Base

class Pet(Base):
    ''' Pet model '''
    __tablename__ = "pet"

    # Pet Fields
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, unique=True)
    age = mapped_column(Integer)

    owner_id = mapped_column(ForeignKey("pet_owner.id"))
    owner = relationship(back_populates="pets")