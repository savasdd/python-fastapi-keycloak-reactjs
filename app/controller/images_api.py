from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Union
from ..database import get_db
from .. import schemas, service_images

router = APIRouter()


@router.get("/movies/{movie_id}/images", response_model=List[schemas.ResponseImage], status_code=status.HTTP_200_OK)
def getAllImage(movie_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    list = service_images.getAllImage(
        db, movie_id=movie_id, skip=skip, limit=limit)
    return list


@router.get("/movies/{movie_id}/images/{id}", response_model=schemas.ResponseImage, status_code=status.HTTP_200_OK)
def getImageById(movie_id: str, id: str, db: Session = Depends(get_db)):
    list = service_images.getImageById(db, movie_id=movie_id, id=id)

    return list


@router.post("/movies/{movie_id}/images", response_model=schemas.ResponseImage, status_code=status.HTTP_201_CREATED)
def createImage(movie_id: str, dto: schemas.CreateImage, db: Session = Depends(get_db)):
    return service_images.createImage(db=db, movie_id=movie_id, dto=dto)


@router.delete("/movies/{movie_id}/images/{id}")
def deleteImage(movie_id: str, id: str, db: Session = Depends(get_db)):
    return service_images.deleteImage(db=db, movie_id=movie_id, id=id)


@router.get('/health')
def root():
    return {'response': 'FastApi Images'}
