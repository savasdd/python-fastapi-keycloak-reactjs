from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from . import models, schemas
import uuid
import base64


def getDetailById(db: Session, car_id: uuid, id: uuid):
    model = db.query(models.CarsDetail).filter(
        models.Cars.id == car_id and models.CarsDetail.id == id).first()
    return model


def getAllDetail(db: Session, car_id: uuid, skip: int = 0, limit: int = 100):
    return db.query(models.CarsDetail).filter(models.Cars.id == car_id).offset(skip).limit(limit).all()


def createDetail(db: Session, car_id: uuid, dto: schemas.CreateDetail):
    model = models.CarsDetail(
        name=dto.name,
        car_id=car_id
    )

    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def deleteDetail(db: Session, car_id: uuid,  id: uuid):
    query = db.query(models.CarsDetail).filter(models.CarsDetail.id == id)
    model = query.first()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'car detail is not foun: {id}')

    if model.car_id != uuid.UUID(car_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='car detail is not found to delete: {car_id}')

    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
