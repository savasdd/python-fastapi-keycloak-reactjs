from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from . import models, schemas
import base64


def getToken(username: str, password: str):
    print(username)
    print(password)

    
    return "Auth"
