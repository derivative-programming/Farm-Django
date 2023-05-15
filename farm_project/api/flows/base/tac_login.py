import uuid
from api.models import Tac 
from api.flows.base import BaseFlow
from api.flows.base import LogSeverity
from api.helpers import SessionContext
 

class BaseFlowTacLogin(BaseFlow):
    def __init__(self, session_context:SessionContext): 
        super(BaseFlowTacLogin, self).__init__(
            "TacLogin", 
            session_context,
            ) 

      
    def _process_validation_rules(self, 
        tac: Tac,
        email: str,
        password: str,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")

        if email == "":
            self._add_field_validation_error(email,"Email is required")
            
        if password == "":
            self._add_field_validation_error(email,"Password is required")

        self._process_security_rules(tac)

    
    def _process_security_rules(self, 
        tac: Tac,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")
