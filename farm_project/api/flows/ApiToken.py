import jwt
import datetime
import os
from django.conf import settings
 

def create_token(payload:dict): 

    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(days=1)

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return token.decode()

def validate_token(token) -> dict:
    try:
        # Decode the token and verify its validity
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return dict()  # The token has expired
    except jwt.InvalidTokenError:
        return dict()  # The token is invalid