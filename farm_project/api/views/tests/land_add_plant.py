from dataclasses import asdict
import json
from django.test import TestCase
from rest_framework.test import APIClient  
import logging
from api.models.factories import LandFactory 
from api.views.factories import LandAddPlantRequestFactory

class LandAddPlantViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient() 
        self.land = LandFactory.create()
        request = LandAddPlantRequestFactory.create()
        self.valid_request_data =  asdict(request)
        self.invalid_request_data = {
            "xxxxxx": "yyyyy" 
        }

    def test_submit_success(self):
        # Assuming you have a FlowLandAddPlant.process method that handles valid data
        logging.debug(f'/api/land-add-plant/{self.land.code}/')
        response = self.client.post(f'/api/land-add-plant/{self.land.code}/', data=self.valid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    def test_submit_failure(self):
        response = self.client.post(f'/api/land-add-plant/{self.land.code}/', data=self.invalid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertFalse(response.data['success'])
        
    def test_submit_failure2(self):
        response = self.client.get('/api/land-add-plant/xxx/')
        self.assertEqual(response.status_code, 404)
        
    def test_submit_failure3(self):
        response = self.client.get('/api/land-add-plant/')
        self.assertEqual(response.status_code, 404)

    def test_init_success(self):
        response = self.client.get(f'/api/land-add-plant/{self.land.code}/init/')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    def test_init_failure(self):
        response = self.client.get('/api/land-add-plant/xxx/init/')
        self.assertEqual(response.status_code, 404)
        
    def test_init_failure2(self):
        response = self.client.get('/api/land-add-plant/init/')
        self.assertEqual(response.status_code, 404)

    # Add any additional test cases for different scenarios and edge cases
