from pydantic import BaseModel
import datetime

from .is_ok_response import IsOkResponse
from .location import Location


class DisasterResponseBase(BaseModel):
    is_ok: IsOkResponse
    message: str
    location: Location
    phone_number: str


class DisasterResponseInput(DisasterResponseBase):
    pass


class DisasterResponseCreate(DisasterResponseInput):
    timestamp: str


class DisasterResponseFireBase(DisasterResponseInput):
    id: str
