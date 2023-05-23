from dataclasses import dataclass, field
from dataclasses_json import dataclass_json,LetterCase 
from .validation_error import ValidationError
from typing import List

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PostResponse:
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)