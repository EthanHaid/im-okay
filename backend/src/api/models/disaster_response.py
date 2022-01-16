from pydantic import BaseModel
import datetime


class DisasterResponseBase(BaseModel):
    is_ok: bool
    message: str
    location: str


class DisasterResponseInput(DisasterResponseBase):
    pass


class DisasterResponseFireBase(DisasterResponseInput):
    id: str
    timestamp: datetime.datetime
