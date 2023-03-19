from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Union
from ..database import get_db
from .. import schemas, service_movies

router = APIRouter()


@router.get("/movies", response_model=List[schemas.ResponseMovie], status_code=status.HTTP_200_OK)
def getAllMovie(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    list = service_movies.getAllMovie(db, skip=skip, limit=limit)
    return list


@router.get("/movies/{id}", response_model=schemas.ResponseMovie, status_code=status.HTTP_200_OK)
def getMovieById(id: str, db: Session = Depends(get_db)):
    list = service_movies.getMovieById(db, id=id)

    return list


@router.post("/movies", response_model=schemas.ResponseMovie, status_code=status.HTTP_201_CREATED)
def createMovie(dto: schemas.CreateMovie, db: Session = Depends(get_db)):
    return service_movies.createMovie(db=db, dto=dto)


@router.put("/movies/{id}", response_model=schemas.ResponseMovie)
def updateMovie(id: str, dto: schemas.CreateMovie, db: Session = Depends(get_db)):
    return service_movies.updateMovie(db=db, dto=dto, id=id)


@router.delete("/movies/{id}")
def deleteMovie(id: str, db: Session = Depends(get_db)):
    return service_movies.deleteMovie(db=db, id=id)

@router.get('/health')
def root():
    return {'response': 'FastApi Movies'}