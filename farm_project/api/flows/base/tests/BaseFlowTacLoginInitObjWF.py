import unittest
from unittest.mock import Mock
from api.models import Tac
from api.flows.base.BaseFlowTacLoginInitObjWF import BaseFlowTacLoginInitObjWF


class BaseFlowTacLoginInitObjWFTestCase(unittest.TestCase):
    def setUp(self):
        self.flow = BaseFlowTacLoginInitObjWF()
    
    def test_process_validation_rules(self):
        # Create a mock Tac object
        tac = Mock(spec=Tac)
        
        # Call the method being tested
        self.flow._process_validation_rules(tac)
        
        # Add assertions here to validate the expected behavior
    
    def test_process_security_rules(self):
        # Create a mock Tac object
        tac = Mock(spec=Tac)
        
        # Call the method being tested
        self.flow._process_security_rules(tac)
        
        # Add assertions here to validate the expected behavior
 