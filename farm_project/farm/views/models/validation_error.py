# views/models/validation_error.py
"""
Validation error model
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json,LetterCase

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidationError:
    """
    Validation error model
    """
    property:str = ""
    message:str  = ""
