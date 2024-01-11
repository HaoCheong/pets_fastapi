"""main.py (5)

Where the endpoints are instantiated and functions are called

- All the data validation are checked here
- Error raising done on this level

"""

from fastapi import FastAPI

import app.database as database
import app.metadata as metadata

from app.database import engine
from fastapi.middleware.cors import CORSMiddleware

import app.endpoints.owner_endpoints as owner_endpoints
import app.endpoints.trainer_endpoints as trainer_endpoints
import app.endpoints.pet_endpoints as pet_endpoints
import app.endpoints.pet_assignment_endpoints as pet_assignment_endpoints
import app.endpoints.nutrition_plan_endpoints as nutrition_plan_endpoints

database.Base.metadata.create_all(bind=engine)

# Initialising instance of the backend
app = FastAPI(
        openapi_tags=metadata.tags_metadata,
        swagger_ui_parameters=metadata.swagger_ui_parameters,
        title=metadata.app_title,
        description=metadata.app_desc,
        version=metadata.app_version,
    )

# Handles CORS, currently available to any origin. Need to be tweaked for security
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======== ROOT ENDPOINT ========
# Not necessary but good indication that connection been made

@app.get("/")
def root():
    return {"connection": True}

app.include_router(owner_endpoints.router)
app.include_router(trainer_endpoints.router)
app.include_router(pet_endpoints.router)
app.include_router(pet_assignment_endpoints.router)
app.include_router(nutrition_plan_endpoints.router)