from sqlalchemy import Column, ForeignKey, Integer, String, JSON, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class NutritionPlan(Base):
    ''' Nutrition plan model '''
    __tablename__ = "nutrition_plan"

    # Nutrition Plan fields
    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String)
    description = Column(String)
    meal = Column(JSON)
    starting_date = Column(DateTime)

    # Pet Relationship (One-to-one)
    pet = relationship("Pet", back_populates="nutrition_plan", uselist=False)