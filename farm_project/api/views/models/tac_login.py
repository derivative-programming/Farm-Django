from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
import uuid
from dataclasses_json import dataclass_json, LetterCase, config  
from api.helpers import TypeConversion
from .post_reponse import PostResponse
from api.flows import FlowTacLoginResult
from api.flows import FlowTacLogin
from api.helpers import SessionContext 
from api.models import Tac 
from api.flows import FlowValidationError
import api.views.models as view_models
import logging
from api.models import Tac 
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass        
class TacLoginPostModelResponse(PostResponse):
    customer_code:uuid = uuid.UUID(int=0)
    email:str = ""
    user_code_value:uuid = uuid.UUID(int=0)
    utc_offset_in_minutes:int = 0
    role_name_csv_list:str = ""
    api_key:str = ""
#endset
    def load_flow_response(self,data:FlowTacLoginResult): 
        placeholder = "" #to avoid pass line
        self.customer_code = data.tac_code
        self.email = data.email
        self.user_code_value = data.tac_
        self.utc_offset_in_minutes = data.utc_offset_in_minutes
        self.role_name_csv_list = data.role_name_csv_list
        self.api_key = data.api_key
#endset
### request. expect camel case. use marshmallow to validate.
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacLoginPostModelRequest:
    email:str = ""
    password:str = ""
#endset 
    def process_request(self,
                        session_context:SessionContext,
                        tac_code:uuid,
                        response:TacLoginPostModelResponse) -> TacLoginPostModelResponse:
        try:
            logging.debug("loading model...")
            tac = Tac.objects.get(code=tac_code)
            flow = FlowTacLogin(session_context)
            logging.debug("process flow...")
            flowResponse = flow.process(
                tac,
                self.email,
                self.password,
#endset
            ) 
            response.load_flow_response(flowResponse); 
            response.success = True
            response.message = "Success."
        except FlowValidationError as ve:
            response.success = False 
            response.validation_errors = list()
            for key in ve.error_dict:
                response.validation_errors.append(view_models.ValidationError(key,ve.error_dict[key]))
        return response

