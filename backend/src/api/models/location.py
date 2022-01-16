from pydantic import BaseModel


class Location(BaseModel):
    lat: str
    lon: str
