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

# images


class ImageBase(BaseModel):
    name: Optional[str]
    movie_id: uuid.UUID | None = None

    class Config:
        orm_mode = True


class CreateImage(ImageBase):
    pass


class ResponseImage(ImageBase):
    id: Optional[uuid.UUID]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ListImage(BaseModel):
    results: int
    data: List[ResponseImage]

# auth


class AuthBase(BaseModel):
    username: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True


class ResponseToken(BaseModel):
    access_token: Optional[str]
    expires_in : Optional[int]
    refresh_token :Optional[str]
    refresh_expires_in: Optional[int]
    token_type : Optional[str]

    class Config:
        orm_mode = True