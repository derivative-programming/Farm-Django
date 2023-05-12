from django.test import TestCase
from api.models import Plant 
 



class PlantTestCase(TestCase):
    def test_plant(self):
        self.assertEquals(
            Plant.objects.count(),
            0
        )
        Plant.objects.create() 
        self.assertEquals(
            Plant.objects.count(),
            1
        ) 