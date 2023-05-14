from django.test import TestCase
from api.models import OrgApiKey 
 



class OrgApiKeyTestCase(TestCase):
    def test_org_api_key(self):
        self.assertEquals(
            OrgApiKey.objects.count(),
            0
        )
        OrgApiKey.objects.create() 
        self.assertEquals(
            OrgApiKey.objects.count(),
            1
        ) 

        
# TODO