from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Union
from ..database import get_db
from .. import schemas, service_auth

router = APIRouter()


@router.post("/auth", response_model=schemas.ResponseToken, status_code=status.HTTP_200_OK)
def createImage(dto: schemas.AuthBase):
    return service_auth.getToken(dto=dto)
