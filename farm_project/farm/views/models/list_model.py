from dataclasses import dataclass
from dataclasses_json import dataclass_json,LetterCase




### response
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ListModel:
    page_number:int = 0
    item_count_per_page:int = 0
    order_by_column_name:str = ""
    order_by_descending:bool = False
    success:bool = False
    records_total:int = 0
    records_filtered:int = 0
    message:str = ""
    app_version:str = ""

