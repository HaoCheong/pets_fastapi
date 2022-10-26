from ctypes import addressof
from unicodedata import name
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

# Pet can belong to 1 owner
# Owner can have many pets

# Pets can belong to many trainer
# Trainers can train many pets

class PetTrainerAssociation(Base):
    __tablename__ = 'pet_trainer_association'
    pet_id = Column(Integer, ForeignKey('Pet.id'), primary_key=True)
    trainer_id = Column(String, ForeignKey('Trrainer.trainer_id'), primary_key=True)

class Owner(Base):
    __tablename__ = "pet_owner"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique = True)
    email = Column(String)
    password = Column(String)
    home_address = Column(String)
    
    pets = relationship("Pet", backref="parent")


class Pet(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, unique = True)
    age = Column(Integer)

    owner_id =Column(Integer, ForeignKey("owner.id"))

    trainers = relationship('Trainer',
                                secondary='pet_trainer_association',
                                primaryjoin=id==PetTrainerAssociation.pet_id,
                                secondaryjoin=id==PetTrainerAssociation.trainer_id,
                                backref='trainers')
    
class Trainer(Base):
    __tablename__ = "trainer"

    trainer_id = Column(String, primary_key = True, index = True)
    name = Column(String)
    phone_no = Column(Integer)
    email = Column(String)

    pets = relationship('Pet',
                            secondary='pet_trainer_association',
                            primaryjoin=id==PetTrainerAssociation.trainer_id,
                            secondaryjoin=id==PetTrainerAssociation.pet_id,
                            backref='pets')