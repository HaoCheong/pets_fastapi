''' Trainer Models

Declarative Base: Used for initialising base fields all models will use

Notes:
- Optional Fields that are either optionally included in the input or optionally NULL on ther return

Relationship:
- Pets: Many Trainers to Many Pets
'''

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.database import Base

from datetime import datetime


class Trainer(Base):
    ''' Trainer model '''
    __tablename__ = "trainer"

    # Trainer Fields
    # Trainer ID is string, thus not auto-generated
    trainer_id: Mapped[str] = mapped_column(
        String, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    phone_no: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    date_started: Mapped[datetime] = mapped_column(DateTime)

    # Pets List (Many-to-Many with association object as link table)
    pets: Mapped[list["Pet"]] = relationship(
        "Pet", secondary="pet_trainer_association", back_populates='trainers')
