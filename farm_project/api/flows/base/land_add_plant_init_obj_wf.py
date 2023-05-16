import uuid
from api.models import Land 
from .base_flow import BaseFlow
from api.flows.base import LogSeverity
from api.helpers import SessionContext
from decimal import Decimal
class BaseFlowLandAddPlantInitObjWF(BaseFlow):
    def __init__(self, session_context:SessionContext): 
        super(BaseFlowLandAddPlantInitObjWF, self).__init__(
            "LandAddPlantInitObjWF", 
            session_context,
            ) 
    def _process_validation_rules(self, 
        land: Land,

        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Validating...")
        self._process_security_rules(land)
    def _process_security_rules(self, 
        land: Land,
        ):
        super()._log_message_and_severity(LogSeverity.information_high_detail, "Processing security rules...")
