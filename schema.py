from typing import Optional
from pydantic import BaseModel


class ServiceBase(BaseModel):
    date: str
    service: str
    availability: float

