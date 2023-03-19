from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from . import models, schemas
import uuid
import base64


def getImageById(db: Session, movie_id: uuid, id: uuid):
    model = db.query(models.MoviesImages).filter(
        models.Movies.id == movie_id and models.MoviesImages.id == id).first()
    return model


def getAllImage(db: Session, movie_id: uuid, skip: int = 0, limit: int = 100):
    return db.query(models.MoviesImages).filter(models.Movies.id == movie_id).offset(skip).limit(limit).all()


def createImage(db: Session, movie_id: uuid, dto: schemas.CreateImage):
    model = models.MoviesImages(
        name=dto.name,
        movie_id=movie_id
    )

    db.add(model)
    db.commit()
    db.refresh(model)
    return model


def deleteImage(db: Session, movie_id: uuid,  id: uuid):
    query = db.query(models.MoviesImages).filter(models.MoviesImages.id == id)
    model = query.first()

    if not model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'image is not foun: {id}')

    if model.movie_id != uuid.UUID(movie_id):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='movie is not found to delete: {movie_id}')

    query.delete(synchronize_session=False)

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
