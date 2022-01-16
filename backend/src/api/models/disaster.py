from pydantic import BaseModel
import datetime
from typing import List
from .disaster_response import DisasterResponseFireBase


class DisasterBase(BaseModel):
    message: str
    location: str
    responses: List[DisasterResponseFireBase]


class DisasterInput(DisasterBase):
    pass


class DisasterFireBase(DisasterBase):
    id: str
    timestamp: datetime.datetime
