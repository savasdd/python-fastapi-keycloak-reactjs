import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Movies(Base):
    __tablename__ = 'movies'
    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    count = Column(Integer, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


class MoviesImages(Base):
    __tablename__ = 'movies_images'
    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    movie_id = Column(UUID(as_uuid=True), ForeignKey(
        'movies.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    movies = relationship('Movies')


class TokenRequest:
    username = str
    password = str


class TokenResponse:
    def __init__(self, access_token: str, expires_in: int, refresh_token: str, refresh_expires_in: int, token_type: str):
        self.access_token = access_token
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.refresh_expires_in = refresh_expires_in
        self.token_type = token_type
