''' Pet Models

Declarative Base: Used for initialising base fields all models will use

Notes:
- Optional Fields that are either optionally included in the input or optionally NULL on ther return

Relationship:
- Owner: Many Pets To One Owner
- Trainer: Many Pets to Many Trainers
- Nutrition Plan: One Pet to One Nutrition Plan
'''

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database.database import Base


class PetTrainerAssociation(Base):
    '''
    Association Table (Pet and Trainer Many-to-Many relationship)
    Done as association object because for future additional data expandability
    '''
    __tablename__ = 'pet_trainer_association'

    # Foreign Keys in Association table
    pet_id: Mapped[int] = mapped_column(ForeignKey('pet.id'), primary_key=True)
    trainer_id: Mapped[str] = mapped_column(
        ForeignKey('trainer.trainer_id'), primary_key=True)


class Pet(Base):
    ''' Pet model '''
    __tablename__ = "pet"

    # Pet Fields

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True)
    age: Mapped[str] = mapped_column(Integer)

    # Owner id (Many-to-One)
    owner_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("pet_owner.id"), nullable=True)
    owner: Mapped["Owner"] = relationship(
        "Owner", back_populates="pets", uselist=False)

    # # Trainer List (Many-to-Many with association object as link table)
    trainers: Mapped[list["Trainer"]] = relationship(
        "Trainer", secondary="pet_trainer_association", back_populates='pets')

    # Nutrition Plan (One-To-One)
    nutrition_plan_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("nutrition_plan.id"), nullable=True)
    nutrition_plan: Mapped["NutritionPlan"] = relationship(
        "NutritionPlan", back_populates="pet", uselist=False)
