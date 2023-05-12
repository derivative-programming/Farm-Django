from django.test import TestCase
from api.models import Flavor 
 



class FlavorTestCase(TestCase):
    def test_flavor(self):
        self.assertEquals(
            Flavor.objects.count(),
            0
        )
        Flavor.objects.create() 
        self.assertEquals(
            Flavor.objects.count(),
            1
        ) 