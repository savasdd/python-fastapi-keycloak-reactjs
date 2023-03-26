from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from .database import get_db
from app.controller import cars_api, detail_api,auth_api


app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_api.router, tags=['Auth'], prefix='/api')
app.include_router(cars_api.router, tags=['Cars'], prefix='/api')
app.include_router(detail_api.router, tags=['Details'], prefix='/api')

