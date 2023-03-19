from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from . import models, schemas
import logging
from keycloak import KeycloakOpenID

SERVER_URL = "http://localhost:8043/auth/"
CLIENT_ID = "food-microservice-backend"
REALM_NAME = "food-microservice"
SECRET_KEY = "8It8vOmZU0iAWEJGbEgowvUaQWSSH523"

log = logging.getLogger()
log.setLevel(logging.INFO)


def getToken(dto: models.TokenRequest):

    keycloak_openid = KeycloakOpenID(
        server_url=SERVER_URL, client_id=CLIENT_ID, realm_name=REALM_NAME, client_secret_key=SECRET_KEY)

    token = keycloak_openid.token(
        username=dto.username,
        password=dto.password,
        grant_type=["password"],
        code="",
        redirect_uri="",
        totp=None,
        scope="openid"
    )

    resp = models.TokenResponse(
        access_token=token['access_token'],
        expires_in=token['expires_in'],
        refresh_token=token['refresh_token'],
        refresh_expires_in=token['refresh_expires_in'],
        token_type=token['token_type']
    )

    log.warn('Generated Token: '+dto.username)
    return resp
