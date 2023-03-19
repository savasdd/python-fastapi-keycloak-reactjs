from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from . import models, schemas
import base64
from keycloak import KeycloakOpenID


def getToken(dto: models.TokenRequest):

    keycloak_openid = KeycloakOpenID(server_url="http://localhost:8043/auth/",
                                     client_id="food-microservice-backend",
                                     realm_name="food-microservice",
                                     client_secret_key="8It8vOmZU0iAWEJGbEgowvUaQWSSH523")

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
        access_token="strfvgyuhjımkoplğş",
        expires_in=1800,
        refresh_token="fgjhkljghjkhjöhöjh",
        refresh_expires_in=2560,
        token_type="Bearer"
    )

    print(token)

    return resp
