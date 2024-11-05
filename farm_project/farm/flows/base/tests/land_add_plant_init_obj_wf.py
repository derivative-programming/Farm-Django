import unittest
from farm.flows.base import BaseFlowLandAddPlantInitObjWF
from farm.helpers import SessionContext
from farm.models.factories import LandFactory
from decimal import Decimal
from farm.models import CurrentRuntime
class BaseFlowLandAddPlantInitObjWFTestCase(unittest.TestCase):
    def setUp(self):
        CurrentRuntime.initialize()
        session_context = SessionContext(dict())
        self.flow = BaseFlowLandAddPlantInitObjWF(session_context)
    def test_process_validation_rules(self):
        land = LandFactory.create()

        # Call the method being tested
        self.flow._process_validation_rules(
            land,

            )
        # Add assertions here to validate the expected behavior
    def test_process_security_rules(self):
        land = LandFactory.create()
        # Call the method being tested
        self.flow._process_security_rules(land)
        # Add assertions here to validate the expected behavior
