from django.test import TestCase
from api.models import Land 
 



class LandTestCase(TestCase):
    def test_land(self):
        self.assertEquals(
            Land.objects.count(),
            0
        )
        Land.objects.create() 
        self.assertEquals(
            Land.objects.count(),
            1
        ) 