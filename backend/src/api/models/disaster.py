from pydantic import BaseModel
import datetime
from typing import List
from .disaster_response import DisasterResponseFireBase


class DisasterBase(BaseModel):
    message: str
    location_string: str


class DisasterInput(DisasterBase):
    pass


class DisasterCreate(DisasterInput):
    timestamp: str


class DisasterFireBase(DisasterBase):
    id: str
    responses: List[DisasterResponseFireBase] = []
