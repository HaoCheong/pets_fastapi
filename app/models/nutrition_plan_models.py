
''' Nutrition Plan Models

Declarative Base: Used for initialising base fields all models will use

Notes:
- Optional Fields that are either optionally included in the input or optionally NULL on ther return

Relationship:
- Nutrition Plan: One Nutrition Plan to One Pet 
'''

from sqlalchemy import Column, Integer, String, JSON, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.database import Base
from datetime import datetime


class NutritionPlan(Base):
    ''' Nutrition plan model '''
    __tablename__ = "nutrition_plan"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column(String)
    meal: Mapped[dict] = mapped_column(JSON)
    starting_date: Mapped[datetime] = mapped_column(DateTime)

    # Pet Relationship (One-to-one)
    pet: Mapped["Pet"] = relationship(
        "Pet", back_populates="nutrition_plan", uselist=False)
