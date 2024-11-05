# helpers/type_conversion.py
"""
This module initializes the type conversion helper used in the project.
"""
from marshmallow import fields
from datetime import date, datetime
import uuid

class TypeConversion:
    """
    This class initializes the type conversion helper used in the project.
    """
    @staticmethod
    def get_default_date():
        """
        This method returns the default date.
        """
        return date(1753,1,1)

    @staticmethod
    def get_default_date_time():
        """
        This method returns the default date time.
        """
        return datetime(1753,1,1,0,0)

    @staticmethod
    def get_default_uuid():
        """
        This method returns the default UUID.
        """
        return uuid.UUID(int=0)



class UUIDField(fields.Field):
    """
    This class initializes the UUID field used in the project.
    """
    def _serialize(self, value, attr, obj, **kwargs):
        """
        This method serializes the UUID field.
        """
        if value is None:
            return ''
        return str(value)

    def _deserialize(self, value, attr, data, **kwargs):
        """
        This method deserializes the UUID field.
        """
        return uuid.UUID(value)
