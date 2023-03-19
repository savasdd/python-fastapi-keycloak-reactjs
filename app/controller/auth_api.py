from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Union
from ..database import get_db
from .. import schemas, service_auth

router = APIRouter()


@router.post("/auth", status_code=status.HTTP_200_OK)
def createImage():
    return service_auth.getToken(username="savas.dede", password="123")
