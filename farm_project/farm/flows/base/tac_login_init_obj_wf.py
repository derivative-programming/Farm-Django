import uuid
from farm.models import Tac 
from .base_flow import BaseFlow
from farm.flows.base import LogSeverity
from farm.helpers import SessionContext
from decimal import Decimal
from datetime import date, datetime
from farm.helpers import TypeConversion

class BaseFlowTacLoginInitObjWF(BaseFlow):
    def __init__(self, session_context:SessionContext): 
        super(BaseFlowTacLoginInitObjWF, self).__init__(
            "TacLoginInitObjWF", 
            session_context,
            ) 
    def _process_validation_rules(self, 
            tac: Tac,

        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")

        self._process_security_rules(tac)
    def _process_security_rules(self, 
        tac: Tac,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")
