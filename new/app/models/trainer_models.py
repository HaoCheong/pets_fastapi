from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from app.database.database import Base


class Trainer(Base):
    ''' Trainer model '''
    __tablename__ = "trainer"

    # Trainer Fields
    # Trainer ID is string, thus not auto-generated
    trainer_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    phone_no = Column(String)
    email = Column(String)
    date_started = Column(DateTime)

    # Pets List (Many-to-Many with association object as link table)
    pets = relationship(
        "Pet", secondary="pet_trainer_association", back_populates='trainers')
