from pydantic import BaseModel


class Disaster(BaseModel):
    id: str
    description: str
    message: str
