from dataclasses import asdict
import json
from django.test import TestCase
from rest_framework.test import APIClient  
import logging
from api.models.factories import LandFactory 
from api.views.factories import LandAddPlantPostModelRequestFactory

class LandAddPlantViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient() 
        self.land = LandFactory.create()
        self.request = LandAddPlantPostModelRequestFactory.create()
        self.valid_request_data =  asdict(self.request)
        self.invalid_request_data = {
            "xxxxxx": "yyyyy" 
        }

        
    def test_post_not_implemented(self):
        # Assuming you have a FlowLandAddPlant.process method that handles valid data
        logging.debug('/api/v1_0/land-add-plant/')
        response = self.client.post('/api/v1_0/land-add-plant/', self.valid_request_data, content_type='application/json')
        self.assertEqual(response.status_code, 501) 

    def test_submit_success(self):
        # Assuming you have a FlowLandAddPlant.process method that handles valid data
        logging.debug(f'/api/v1_0/land-add-plant/{self.land.code}/')
        response = self.client.post(f'/api/v1_0/land-add-plant/{self.land.code}/submit/', data=self.request.to_json(), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    def test_submit_failure(self):
        response = self.client.post(f'/api/v1_0/land-add-plant/{self.land.code}/submit/', data=self.invalid_request_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertFalse(response.data['success'])
        
    def test_submit_failure2(self):
        response = self.client.get('/api/v1_0/land-add-plant/xxx/')
        self.assertEqual(response.status_code, 404)
        
    def test_submit_failure3(self):
        response = self.client.get('/api/v1_0/land-add-plant/')
        self.assertEqual(response.status_code, 501)

    def test_init_success(self):
        response = self.client.get(f'/api/v1_0/land-add-plant/{self.land.code}/init/')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    def test_init_failure(self):
        response = self.client.get('/api/v1_0/land-add-plant/xxx/init/')
        self.assertEqual(response.status_code, 404)
        
    def test_init_failure2(self):
        response = self.client.get('/api/v1_0/land-add-plant/init/')
        self.assertEqual(response.status_code, 404)

    # Add any additional test cases for different scenarios and edge cases
