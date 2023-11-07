# from sqlalchemy.orm import Session

# from fastapi.encoders import jsonable_encoder



# def create_pet(db: Session, pet: schema.PetCreate):
#     ''' Creating an new pet '''
#     db_pet = models.Pet(
#         name=pet.name,
#         age=pet.age,
#     )

#     db.add(db_pet)
#     db.commit()
#     db.refresh(db_pet)
#     return db_pet


# def get_all_pets(db: Session, skip: int = 0, limit: int = 100):
#     ''' Get every instance of pet, using offset pagination '''
#     return db.query(models.Pet).offset(skip).limit(limit).all()


# def get_pet_by_id(db: Session, id: int):
#     ''' Get specific instance of pet based on provided pet ID '''
#     return db.query(models.Pet).filter(models.Pet.id == id).first()


# def update_pet_by_id(db: Session, id: int, new_pet: schema.PetUpdate):
#     ''' Update specific fields of specified instance of pet on provided pet ID '''
#     db_pet = db.query(models.Pet).filter(models.Pet.id == id).first()

#     # Converts new_pet from model.object to dictionary
#     update_pet = new_pet.dict(exclude_unset=True)

#     # Loops through dictionary and update db_pet
#     for key, value in update_pet.items():
#         setattr(db_pet, key, value)

#     db.add(db_pet)
#     db.commit()
#     db.refresh(db_pet)
#     return db_pet


# def delete_pet_by_id(db: Session, id: int):
#     ''' Delete specified instance of pet on provided pet ID '''
#     db_pet = db.query(models.Pet).filter(models.Pet.id == id).first()

#     db.delete(db_pet)
#     db.commit()
#     return {"Success": True}