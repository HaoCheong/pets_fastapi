from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base


class PetTrainerAssociation(Base):
    '''
    Association Table (Pet and Trainer Many-to-Many relationship)
    Done as association object because for future additional data expandability
    '''
    __tablename__ = 'pet_trainer_association'

    # Foreign Keys in Association table
    pet_id = Column(ForeignKey('pet.id'), primary_key=True)
    trainer_id = Column(ForeignKey('trainer.trainer_id'), primary_key=True)


class Pet(Base):
    ''' Pet model '''
    __tablename__ = "pet"

    # Pet Fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    age = Column(Integer)

    # Owner id (Many-to-One)
    owner_id = Column(Integer, ForeignKey("pet_owner.id"))
    owner = relationship("Owner", back_populates="pets", uselist=False)

    # Trainer List (Many-to-Many with association object as link table)
    trainers = relationship(
        "Trainer", secondary="pet_trainer_association", back_populates='pets')

    # Nutrition Plan (One-To-One)
    nutrition_plan_id = Column(Integer, ForeignKey("nutrition_plan.id"))
    nutrition_plan = relationship(
        "NutritionPlan", back_populates="pet", uselist=False)
