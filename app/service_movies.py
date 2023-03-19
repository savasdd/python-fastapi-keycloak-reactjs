from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from . import models, schemas
import uuid
import base64


def getMovieById(db: Session, id: uuid):
    model = db.query(models.Movies).filter(
        models.Movies.id == id).first()
    return model


def getAllMovie(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Movies).offset(skip).limit(limit).all()


def createMovie(db: Session, dto: schemas.CreateMovie):
    model = models.Movies(
        name=dto.name,
        count=dto.count,
        price=dto.price,
        description=dto.description)

    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def updateMovie(db: Session, dto: schemas.CreateMovie, id: uuid):
    query = db.query(models.Movies).filter(models.Movies.id == id)
    model = query.first()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'movie is not foun: {id}')

    update_data = dto.dict(exclude_unset=True)
    query.filter(models.Movies.id == id).update(
        update_data, synchronize_session=False)

    db.commit()
    db.refresh(model)

    return model


def deleteMovie(db: Session,  id: uuid):
    query = db.query(models.Movies).filter(models.Movies.id == id)
    model = query.first()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'movie is not foun: {id}')

    query.delete(synchronize_session=False)

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
