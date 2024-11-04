from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

# ========== MODEL ==========

class PetBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

# ========== SCHEMA ==========

class Pet(PetBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nickname: str

class PetRead(PetBase):
    id: int

class PetCreate(PetBase):
    nickname: str

class PetUpdate(PetBase):
    name: str | None = None
    age: int | None = None
    nickname: str | None = None

# ========== DATABASE ==========

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    ''' Instantiate the database tables '''
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# ========== SESSION ==========
SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

# ========== ENDPOINTS ==========

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/pet/", response_model=PetRead)
def create_pet(pet: PetCreate, session: SessionDep):

    db_pet = Pet.model_validate(pet)

    session.add(db_pet)
    session.commit()
    session.refresh(db_pet)

    return db_pet

@app.get("/pets/", response_model=list[PetRead])
def read_pets(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100) -> list[Pet]:
    pet = session.exec(select(Pet).offset(offset).limit(limit)).all()
    return pet

@app.get("/pet/{pet_id}", response_model=list[PetRead])
def read_pet(pet_id: int, session: SessionDep):

    pet = session.get(Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    return pet

@app.patch("/pet/{pet_id}", response_model=PetRead)
def update_pet(pet_id: int, pet: PetUpdate, session: SessionDep):
    pet_db = session.get(Pet, pet_id)
    if not pet_db:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    pet_data = pet.model_dump(exclude_unset=True)
    pet_db.sqlmodel_update(pet_data)

    session.add(pet_db)
    session.commit()
    session.refresh(pet_db)

    return pet_db

@app.delete("/pet/{pet_id}")
def delete_pet(pet_id: int, session: SessionDep):

    pet = session.get(Pet, pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    
    session.delete(pet)
    session.commit()

    return {"Success": True}