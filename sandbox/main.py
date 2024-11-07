from typing import List, Optional
from fastapi.exceptions import HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, Relationship
from fastapi import FastAPI, Depends
import uvicorn

# ==================== TEAM ====================

class TeamBase(SQLModel):
    team_name: str


class Team(TeamBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
    heroes: List["Hero"] = Relationship(back_populates="team")

    def hero_ids(self):
        return [hero.id for hero in self.heroes]
  
class TeamRead(TeamBase):
    id: int

# ==================== HERO ====================

class HeroBase(SQLModel):
    hero_name: str
    team_id: Optional[int] = Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    team: Optional[Team] = Relationship(back_populates="heroes")


class HeroRead(HeroBase):
    id: int 

# ==================== TEAM READ ====================

class TeamReadWithHeroes(TeamRead):
    heroes: List["HeroRead"] = []

# ==================== HERO READ ====================

class HeroReadWithTeam(HeroRead):
    team: Optional[TeamRead] = None


# engine = create_engine("postgresql://postgres:mysecretpassword@localhost:5432/testdb", echo=True)
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

t1 = Team(team_name="t1")
h1 = Hero(hero_name="h1", team=t1)
h2 = Hero(hero_name="h2", team=t1)

def get_session():
    with Session(engine) as session:
        yield session
 
app = FastAPI()

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(t1)
        session.commit()
        session.refresh(t1)
 

@app.get("/team/{team_id}", response_model=TeamReadWithHeroes)
def home(*, team_id: int, session: Session = Depends(get_session)):
    team = session.get(Team, team_id)
    print(team)
    return team 

@app.get("/heroes/{hero_id}", response_model=HeroReadWithTeam)
def read_hero(*, hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero

@app.get("/teamheroids/{team_id}")
def read_team_heroids(*, team_id: int, session: Session = Depends(get_session)):
    team = session.get(Team, team_id)
    print(team.hero_ids())
    return(team.hero_ids())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)