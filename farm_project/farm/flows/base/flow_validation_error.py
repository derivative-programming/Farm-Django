# flows/base/flow_validation_error.py
"""
This module initializes the flow validation error used in the project.
"""
from dataclasses import dataclass


@dataclass
class FlowValidationError(Exception):
    """
    This class initializes the flow validation error used in the project.
    """
    error_dict:dict

    def __init__(self, field_name:str, message:str, error_dict:dict):
        """
        This method initializes the flow validation error used in the project.
        """
        if error_dict is not None:
            self.error_dict = error_dict
            message = next(iter(error_dict.values()))
            super().__init__(message)
        elif field_name is not None and message is not None:
            self.error_dict = dict()
            self.error_dict[field_name] = message
            super().__init__(message)
        elif message is not None:
            self.error_dict = dict()
            self.error_dict[""] = message
            super().__init__(message)
