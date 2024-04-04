import uuid

from pydantic import BaseModel


class Course(BaseModel):
    id: uuid.UUID
    name: str
    location: str
    holes: int
