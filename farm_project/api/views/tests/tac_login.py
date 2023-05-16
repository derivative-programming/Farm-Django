from django.test import TestCase
from rest_framework.test import APIClient 
from api.models import Customer 
from api.views import TacLoginViewSet
from uuid import uuid4
import logging
import json
from api.models.factories import TacFactory

class TacLoginViewSetTestCase(TestCase):

    def setUp(self):
        logging.debug("TacLoginViewSetTestCase setup")
        self.client = APIClient() 
        self.tac = TacFactory.create()
        self.customer = Customer.objects.create(code=uuid4(), first_name="Test first name", email="test@example.com", password="test_password")
        self.customer.tac = self.tac 
        self.customer.save()
        logging.debug(str(self.customer))
        self.valid_request_data = {
            "email": "test@example.com",
            "password": "test_password"
        }
        self.invalid_request_data = {
            "emailxxx": "invalid@example.com",
            "passwordxxx": "wrong_password"
        }

    def test_submit_success(self):
        # Assuming you have a FlowTacLogin.process method that handles valid data
        logging.debug(f'/api/tac-login/{self.tac.code}/')
        response = self.client.post(f'/api/tac-login/{self.tac.code}/', data=self.valid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(responseDict["success"]) 

    def test_submit_failure(self):
        response = self.client.post(f'/api/tac-login/{self.tac.code}/', data=self.invalid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertFalse(response.data['success'])
        
    def test_submit_failure2(self):
        response = self.client.get('/api/tac-login/xxx/')
        self.assertEqual(response.status_code, 404)
        
    def test_submit_failure3(self):
        response = self.client.get('/api/tac-login/')
        self.assertEqual(response.status_code, 404)

    def test_init_success(self):
        response = self.client.get(f'/api/tac-login/{self.tac.code}/init/')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    def test_init_failure(self):
        response = self.client.get('/api/tac-login/xxx/init/')
        self.assertEqual(response.status_code, 404)
        
    def test_init_failure2(self):
        response = self.client.get('/api/tac-login/init/')
        self.assertEqual(response.status_code, 404)

    # Add any additional test cases for different scenarios and edge cases
