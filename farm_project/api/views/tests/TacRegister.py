import json
from django.test import TestCase
from rest_framework.test import APIClient
from api.models import Tac
from api.views.TacRegister import TacRegisterViewSet
from uuid import uuid4
import logging

class TacRegisterViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.tac = Tac.objects.create(code=uuid4(), name="Test Tac")
        self.valid_request_data = {
            "email": "test@example.com",
            "password": "test_password",
            "confirmPassword": "test_password",
            "firstName": "test_first_name",
            "lastName": "test_last_name",
        }
        self.invalid_request_data = {
            "emailxxx": "invalid@example.com",
            "password": "wrong_password"
        }

    def test_submit_success(self):
        # Assuming you have a FlowTacRegister.process method that handles valid data
        logging.debug(f'/api/tac-register/{self.tac.code}/')
        response = self.client.post(f'/api/tac-register/{self.tac.code}/', data=self.valid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    def test_submit_failure(self):
        response = self.client.post(f'/api/tac-register/{self.tac.code}/', data=self.invalid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertFalse(response.data['success'])
        
    def test_submit_failure2(self):
        response = self.client.get('/api/tac-register/xxx/')
        self.assertEqual(response.status_code, 404)
        
    def test_submit_failure3(self):
        response = self.client.get('/api/tac-register/')
        self.assertEqual(response.status_code, 404)

    def test_init_success(self):
        response = self.client.get(f'/api/tac-register/{self.tac.code}/init/')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    def test_init_failure(self):
        response = self.client.get('/api/tac-register/xxx/init/')
        self.assertEqual(response.status_code, 404)
        
    def test_init_failure2(self):
        response = self.client.get('/api/tac-register/init/')
        self.assertEqual(response.status_code, 404)

    # Add any additional test cases for different scenarios and edge cases
