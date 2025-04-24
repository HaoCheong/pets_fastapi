from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base

# Owner Table


class Owner(Base):
    ''' Owner model '''
    __tablename__ = "pet_owner"

    # Owner Fields
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String)
    password = Column(String)
    home_address = Column(String)

    # Pet relation (One-to-Many)
    pets = relationship("Pet", back_populates="owner")
