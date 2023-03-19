from datetime import datetime
from typing import List, Union
import uuid
from pydantic import BaseModel, EmailStr, constr
from pydantic.schema import Optional, Dict


class MovieBase(BaseModel):
    name: Optional[str]
    count: Optional[int]
    price: Optional[float]

    class Config:
        orm_mode = True


class CreateMovie(MovieBase):
    description: str | None = None


class ResponseMovie(MovieBase):
    id: Optional[uuid.UUID]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ListMovie(BaseModel):
    results: int
    data: List[ResponseMovie]
