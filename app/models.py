import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, String, Boolean, text, Integer, Float, DATE
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Cars(Base):
    __tablename__ = 'cars'
    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    seri = Column(String, nullable=True)
    model = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    km = Column(Float, nullable=True)
    color = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    advertDate = Column(DATE, nullable=True)
    description = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))


class CarsDetail(Base):
    __tablename__ = 'cars_detail'
    id = Column(UUID(as_uuid=True), primary_key=True,
                nullable=False, default=uuid.uuid4)
    name = Column(String, nullable=False)
    car_id = Column(UUID(as_uuid=True), ForeignKey(
        'cars.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    cars = relationship('Cars')


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
