from pydantic import BaseModel


class Location(BaseModel):
    lat: int
    lon: int
