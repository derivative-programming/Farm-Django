# views/models/post_response.py
"""
This module initializes the post response model used in the project.
"""
from typing import List
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json,LetterCase
from .validation_error import ValidationError

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PostResponse:
    """
    Post response model.
    """
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)
