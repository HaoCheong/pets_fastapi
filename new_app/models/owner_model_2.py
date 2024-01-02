from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import String

from app.database import Base

# Owner Table
class Owner(Base):
    ''' Owner model '''
    __tablename__ = "pet_owner"

    # Owner Fields
    id = mapped_column(Integer, primary_key=True, index=True)
    name = mapped_column(String, unique=True)
    email = mapped_column(String)
    password = mapped_column(String)
    home_address = mapped_column(String)

    # Pet relation (One-to-Many)
    pets = relationship(back_populates="Owner")

    