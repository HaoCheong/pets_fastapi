from typing import Annotated

from fastapi import Depends, FastAPI
from sqlmodel import Session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()
