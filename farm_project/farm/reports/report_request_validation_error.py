# reports/report_request_validation_error.py
"""
Tthe report request validation error.
"""
from dataclasses import dataclass

@dataclass
class ReportRequestValidationError(Exception):
    """
    The report request validation error.
    """
    error_dict:dict


    def __init__(self, field_name:str, message:str):
        """
        Initializes the report request validation error.
        """
        if field_name is not None and message is not None:
            self.error_dict = dict()
            self.error_dict[field_name] = message
            super().__init__(message)
        elif message is not None:
            self.error_dict = dict()
            self.error_dict[""] = message
            super().__init__(message)
