import uuid

from pydantic import BaseModel


class Player(BaseModel):
    id: uuid.UUID
    name:str
    handicapp: float
