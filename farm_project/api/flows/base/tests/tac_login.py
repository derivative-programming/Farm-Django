import unittest   
from api.flows.base import BaseFlowTacLogin
from api.helpers import SessionContext
from api.models.factories import TacFactory


class BaseFlowTacLoginTestCase(unittest.TestCase):
    def setUp(self):
        session_context = SessionContext(dict())
        self.flow = BaseFlowTacLogin(session_context)
    
    def test_process_validation_rules(self):
        # Create a mock Tac object
        # pac = Mock(spec=Pac)
        # tac = Mock(spec=Tac)
        # tac.pac.return_value = pac
        tac = TacFactory.create()
        email = "test@example.com"
        password = "password123"
        
        # Call the method being tested
        self.flow._process_validation_rules(tac, email, password)
        
        # Add assertions here to validate the expected behavior
    
    def test_process_security_rules(self):
        # Create a mock Tac object
        # pac = Mock(spec=Pac)
        # tac = Mock(spec=Tac)
        # tac.pac.return_value = pac
        tac = TacFactory.create()
        
        # Call the method being tested
        self.flow._process_security_rules(tac)
        
        # Add assertions here to validate the expected behavior
