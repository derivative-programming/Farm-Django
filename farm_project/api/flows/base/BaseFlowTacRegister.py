import uuid
from api.models import Tac 
from .BaseFlow import BaseFlow
from api.flows.base.LogSeverity import LogSeverity

class BaseFlowTacRegister(BaseFlow):
    def __init__(self): 
        super(BaseFlowTacRegister, self).__init__("TacRegister") 
     
    
    def _process_validation_rules(self, 
        tac: Tac,
        email:str,
        password:str,
        confirm_password:str,
        first_name:str,
        last_name:str,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")
        self._process_security_rules(tac)
        

    
    def _process_security_rules(self, 
        tac: Tac,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")
