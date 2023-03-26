from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Union
from ..database import get_db
from .. import schemas, service_cars

router = APIRouter()


@router.get("/cars", response_model=List[schemas.ResponseCar], status_code=status.HTTP_200_OK)
def getAllCar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    list = service_cars.getAllCar(db, skip=skip, limit=limit)
    return list


@router.get("/cars/{id}", response_model=schemas.ResponseCar, status_code=status.HTTP_200_OK)
def getCarById(id: str, db: Session = Depends(get_db)):
    list = service_cars.getCarById(db, id=id)

    return list


@router.post("/cars", response_model=schemas.ResponseCar, status_code=status.HTTP_201_CREATED)
def createCar(dto: schemas.CreateCar, db: Session = Depends(get_db)):
    return service_cars.createCar(db=db, dto=dto)


@router.put("/cars/{id}", response_model=schemas.ResponseCar)
def updateCar(id: str, dto: schemas.CreateCar, db: Session = Depends(get_db)):
    return service_cars.updateCar(db=db, dto=dto, id=id)


@router.delete("/cars/{id}")
def deleteCar(id: str, db: Session = Depends(get_db)):
    return service_cars.deleteCar(db=db, id=id)


@router.get('/health')
def root():
    return {'response': 'FastApi Movies'}
