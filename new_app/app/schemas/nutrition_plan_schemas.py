from sqlmodel import Field

from datetime import datetime

import app.models.nutrition_plan_models as models



class NutritionPlanReadNR(models.NutritionPlanBase):
    id: int
    starting_date: datetime 

class NutritionPlanReadWR(NutritionPlanReadNR):
    pass

class NutritionPlanCreate(models.NutritionPlanBase):
    starting_date: datetime 

class NutritionPlanUpdate(models.NutritionPlanBase):
    name: str | None = None
    description: str | None = None
    meal: str | None = None
    starting_date: datetime | None = None
