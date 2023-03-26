from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Union
from ..database import get_db
from .. import schemas, service_car_details

router = APIRouter()


@router.get("/cars/{car_id}/details", response_model=List[schemas.ResponseDetail], status_code=status.HTTP_200_OK)
def getAllDetail(car_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    list = service_car_details.getAllDetail(
        db, car_id=car_id, skip=skip, limit=limit)
    return list


@router.get("/cars/{car_id}/details/{id}", response_model=schemas.ResponseDetail, status_code=status.HTTP_200_OK)
def getDetailById(car_id: str, id: str, db: Session = Depends(get_db)):
    list = service_car_details.getDetailById(db, car_id=car_id, id=id)

    return list


@router.post("/cars/{car_id}/details", response_model=schemas.ResponseDetail, status_code=status.HTTP_201_CREATED)
def createDetail(car_id: str, dto: schemas.CreateDetail, db: Session = Depends(get_db)):
    return service_car_details.createDetail(db=db, car_id=car_id, dto=dto)


@router.delete("/cars/{car_id}/details/{id}")
def deleteDetail(car_id: str, id: str, db: Session = Depends(get_db)):
    return service_car_details.deleteDetail(db=db, car_id=car_id, id=id)


@router.get('/health')
def root():
    return {'response': 'FastApi Details'}
