# from sqlalchemy.orm import Session
# import app.model as models
# import app.schemas as schemas
# from fastapi.encoders import jsonable_encoder


# def create_trainer(db: Session, trainer: schemas.TrainerCreate):
#     ''' Creating an new pet trainer '''
#     db_trainer = models.Trainer(
#         trainer_id=trainer.trainer_id,
#         name=trainer.name,
#         description=trainer.description,
#         phone_no=trainer.phone_no,
#         email=trainer.email,
#         date_started=trainer.date_started
#     )

#     db.add(db_trainer)
#     db.commit()
#     db.refresh(db_trainer)
#     return db_trainer


# def get_all_trainers(db: Session, skip: int = 0, limit: int = 100):
#     ''' Get every instance of pet trainer, using offset pagination '''
#     return db.query(models.Trainer).offset(skip).limit(limit).all()


# def get_trainer_by_id(db: Session, trainer_id: str):
#     ''' Get specific instance of pet trainer based on provided trainer ID '''
#     return db.query(models.Trainer).filter(models.Trainer.trainer_id == trainer_id).first()


# def update_trainer_by_id(db: Session, trainer_id: str, new_trainer: schemas.TrainerUpdate):
#     ''' Update specific fields of specified instance of pet trainer on provided trainer ID '''
#     db_trainer = db.query(models.Trainer).filter(
#         models.Trainer.trainer_id == trainer_id).first()

#     # Converts new_trainer from model.object to dictionary
#     update_trainer = new_trainer.dict(exclude_unset=True)

#     # Loops through dictionary and update db_trainer
#     for key, value in update_trainer.items():
#         setattr(db_trainer, key, value)

#     db.add(db_trainer)
#     db.commit()
#     db.refresh(db_trainer)
#     return db_trainer


# def delete_trainer_by_id(db: Session, trainer_id: str):
#     ''' Delete specified instance of pet trainer on provided trainer ID '''
#     db_trainer = db.query(models.Trainer).filter(
#         models.Trainer.trainer_id == trainer_id).first()

#     db.delete(db_trainer)
#     db.commit()
#     return {"Success": True}