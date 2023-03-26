from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from . import models, schemas
import uuid


def getCarById(db: Session, id: uuid):
    model = db.query(models.Cars).filter(
        models.Cars.id == id).first()
    return model


def getAllCar(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Cars).offset(skip).limit(limit).all()


def createCar(db: Session, dto: schemas.CreateCar):
    model = models.Cars(
        name=dto.name,
        seri=dto.seri,
        model=dto.model,
        year=dto.year,
        km=dto.km,
        color=dto.color,
        price=dto.price,
        description=dto.description)

    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def updateCar(db: Session, dto: schemas.CreateCar, id: uuid):
    query = db.query(models.Cars).filter(models.Cars.id == id)
    model = query.first()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'car is not foun: {id}')

    update_data = dto.dict(exclude_unset=True)
    query.filter(models.Cars.id == id).update(
        update_data, synchronize_session=False)

    db.commit()
    db.refresh(model)

    return model


def deleteCar(db: Session,  id: uuid):
    query = db.query(models.Cars).filter(models.Cars.id == id)
    model = query.first()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'car is not foun: {id}')

    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
