# helpers/api_token.py
"""
This module initializes the API token helper used in the project.
"""
import jwt
import datetime
import os
from django.conf import settings
import logging

class ApiToken:
    """
    This class initializes the API token helper used in the project.
    """

    @staticmethod
    def create_token(payload:dict, expires_in_day_count:int):
        """
        This method creates a new token.
        """
        logging.debug("create_token Start")

        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(days=expires_in_day_count)

        logging.debug(str(payload))
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        logging.debug("create_token: " + token)
        logging.debug("create_token End")
        return token

    @staticmethod
    def validate_token(token) -> dict:
        """
        This method validates the token.
        """
        try:
            # Decode the token and verify its validity
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return dict()  # The token has expired
        except jwt.InvalidTokenError:
            return dict()  # The token is invalid
