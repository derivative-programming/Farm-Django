from django.test import TestCase
from dataclasses import asdict
from rest_framework.test import APIClient 
from api.views.fs_farm_api.v1_0 import LandPlantListViewSet
from uuid import uuid4
import logging
import json
from api.models.factories import LandFactory
from api.views.factories import LandPlantListGetModelRequestFactory

class LandPlantListViewSetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient() 
        self.land = LandFactory.create()
        request = LandPlantListGetModelRequestFactory.create()
        self.valid_request_data =  asdict(request)
        self.invalid_request_data = {
            "xxxxxx": "yyyyy" 
        }

        self.invalid_request_data2 =  asdict(request) 
        self.invalid_request_data2["itemCountPerPage"] = "0"

        self.invalid_request_data3 = asdict(request)
        self.invalid_request_data3["pageNumber"] = "0"

    def test_submit_success(self):
        logging.debug('LandPlantListViewSetTestCase test_submit_success')
        # Assuming you have a FlowLandPlantList.process method that handles valid data 
        response = self.client.get(f'/api/v1_0/land-plant-list/{self.land.code}/', data=self.valid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(responseDict['success'])

    def test_submit_failure(self):
        logging.debug('LandPlantListViewSetTestCase test_submit_failure')
        response = self.client.get(f'/api/v1_0/land-plant-list/{self.land.code}/', data=self.invalid_request_data, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertFalse(response.data['success'])
        
    
    def test_submit_failure2(self):
        response = self.client.get('/api/v1_0/land-plant-list/xxx/')
        self.assertEqual(response.status_code, 404) 

    def test_submit_failure3(self):
        response = self.client.get('/api/v1_0/land-plant-list/')
        self.assertEqual(response.status_code, 404)
        

    def test_submit_failure4(self):
        response = self.client.get(f'/api/v1_0/land-plant-list/{self.land.code}/', data=self.invalid_request_data2, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertFalse(response.data['success'])
        

    def test_submit_failure5(self):
        response = self.client.get(f'/api/v1_0/land-plant-list/{self.land.code}/', data=self.invalid_request_data3, format='json')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertFalse(response.data['success'])

    def test_init_success(self):
        response = self.client.get(f'/api/v1_0/land-plant-list/{self.land.code}/init/')
        self.assertEqual(response.status_code, 200)
        json_string = response.content.decode() 
        responseDict = json.loads(json_string) 
        self.assertTrue(response.data['success'])

    
    def test_init_failure(self):
        response = self.client.get('/api/v1_0/land-plant-list/xxx/init/')
        self.assertEqual(response.status_code, 404)
        
    def test_init_failure2(self):
        response = self.client.get('/api/v1_0/land-plant-list/init/')
        self.assertEqual(response.status_code, 404)

    # Add any additional test cases for different scenarios and edge cases
