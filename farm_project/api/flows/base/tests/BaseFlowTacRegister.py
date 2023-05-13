import unittest
from unittest.mock import Mock
from api.models import Pac
from api.models import Tac
from api.flows.base.BaseFlowTacRegister import BaseFlowTacRegister
from api.helpers import SessionContext


class BaseFlowTacRegisterTestCase(unittest.TestCase):
    def setUp(self):
        session_context = SessionContext(dict())
        self.flow = BaseFlowTacRegister(session_context)
    
    def test_process_validation_rules(self):
        # Create a mock Tac object
        pac = Mock(spec=Pac)
        tac = Mock(spec=Tac)
        tac.pac.return_value = pac
        email = "test@example.com"
        password = "password123"
        confirm_password = "password123"
        first_name = "John"
        last_name = "Doe"
        
        # Call the method being tested
        self.flow._process_validation_rules(tac, email, password, confirm_password, first_name, last_name)
        
        # Add assertions here to validate the expected behavior
    
    def test_process_security_rules(self):
        # Create a mock Tac object
        pac = Mock(spec=Pac)
        tac = Mock(spec=Tac)
        tac.pac.return_value = pac
        
        # Call the method being tested
        self.flow._process_security_rules(tac)
        
        # Add assertions here to validate the expected behavior
