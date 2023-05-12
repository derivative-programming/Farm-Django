from django.test import TestCase
from api.models import Pac 
 



class PacTestCase(TestCase):
    def test_pac(self):
        self.assertEquals(
            Pac.objects.count(),
            0
        )
        Pac.objects.create() 
        self.assertEquals(
            Pac.objects.count(),
            1
        ) 