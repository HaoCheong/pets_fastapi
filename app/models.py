"""models.py (2)

Python class which gets translated into actual DB ttables

Terms:
- Base: Indicate a table
- __tablename__: Name of the table that will be created

"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


# Association Table (Pet and Trainer Many-to-Many relationship)
# Done as association object because for future additional data expandability
class PetTrainerAssociation(Base):
    __tablename__ = 'pet_trainer_association'

    # Foreign Keys in Association table
    pet_id = Column(ForeignKey('pet.id'), primary_key=True)
    trainer_id = Column(ForeignKey('trainer.trainer_id'), primary_key=True)

# Owner Table


class Owner(Base):
    __tablename__ = "pet_owner"

    # Owner Fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    home_address = Column(String)

    # Pet relation (One-to-Many)
    pets = relationship("Pet", backref="owner")

# Pet Table


class Pet(Base):
    __tablename__ = "pet"

    # Pet Fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    age = Column(Integer)

    # Owner id (Many-to-One)
    owner_id = Column(Integer, ForeignKey("pet_owner.id"))

    # Trainer List (Many-to-Many with association object as link table)
    trainers = relationship(
        "Trainer", secondary="pet_trainer_association", back_populates='pets')


class Trainer(Base):
    __tablename__ = "trainer"

    # Pet Fields
    # Trainer ID is string
    trainer_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    phone_no = Column(Integer)
    email = Column(String)

    # Pets List (Many-to-Many with association object as link table)
    pets = relationship(
        "Pet", secondary="pet_trainer_association", back_populates='trainers')
