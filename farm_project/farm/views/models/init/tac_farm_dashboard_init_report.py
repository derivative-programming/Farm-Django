from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from farm.views.models import ValidationError
from typing import List
import uuid
from dataclasses_json import dataclass_json, LetterCase, config    
from farm.helpers import TypeConversion 
from farm.flows import FlowTacFarmDashboardInitReportResult 
from farm.helpers import SessionContext 
from farm.models import Tac 
from farm.flows import FlowTacFarmDashboardInitReport 
from farm.flows import FlowValidationError
import farm.views.models as view_models
import logging
from farm.models import Tac 
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacFarmDashboardInitReportGetInitModelResponse():
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)
    customerCode:uuid.UUID = field(default_factory=lambda: uuid.UUID('00000000-0000-0000-0000-000000000000'))
#endset
    def load_flow_response(self,data:FlowTacFarmDashboardInitReportResult): 
        self.validation_errors = list()
        self.success = False
        self.message = ""
        self.customerCode = data.customer_code
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacFarmDashboardInitReportGetInitModelRequest():
    def process_request(self,
                        session_context:SessionContext,
                        tac_code:uuid,
                        response:TacFarmDashboardInitReportGetInitModelResponse) -> TacFarmDashboardInitReportGetInitModelResponse:
        try:
            logging.debug("loading model...")
            tac = Tac.objects.get(code=tac_code)
            logging.debug("process request...") 
            flow = FlowTacFarmDashboardInitReport(session_context)
            flowResponse = flow.process(
                tac
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

