from datetime import datetime
from datetime import date
from typing import List, Union
import uuid
from pydantic import BaseModel, EmailStr, constr
from pydantic.schema import Optional, Dict


class CarBase(BaseModel):
    name: Optional[str]
    seri: Optional[str]
    model: Optional[str]
    year: Optional[int]
    km: Optional[float]
    color: Optional[str]
    price: Optional[float]
    advertDate:Optional[date]

    class Config:
        orm_mode = True


class CreateCar(CarBase):
    description: str | None = None


class ResponseCar(CarBase):
    id: Optional[uuid.UUID]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ListCar(BaseModel):
    results: int
    data: List[ResponseCar]

# images


class DetailBase(BaseModel):
    name: Optional[str]
    car_id: uuid.UUID | None = None

    class Config:
        orm_mode = True


class CreateDetail(DetailBase):
    pass


class ResponseDetail(DetailBase):
    id: Optional[uuid.UUID]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class ListDetail(BaseModel):
    results: int
    data: List[ResponseDetail]

# auth


class AuthBase(BaseModel):
    username: Optional[str]
    password: Optional[str]

    class Config:
        orm_mode = True


class ResponseToken(BaseModel):
    access_token: Optional[str]
    expires_in: Optional[int]
    refresh_token: Optional[str]
    refresh_expires_in: Optional[int]
    token_type: Optional[str]

    class Config:
        orm_mode = True
