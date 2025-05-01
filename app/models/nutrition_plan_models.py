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
    meal: Mapped[str] = mapped_column(String)
    starting_date: Mapped[datetime] = mapped_column(DateTime)

    # Pet Relationship (One-to-one)
    # pet = relationship("Pet", back_populates="nutrition_plan", uselist=False)
