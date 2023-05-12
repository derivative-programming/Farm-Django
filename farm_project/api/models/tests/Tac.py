from django.test import TestCase
from api.models import Tac 
 



class TacTestCase(TestCase):
    def test_tac(self):
        self.assertEquals(
            Tac.objects.count(),
            0
        )
        Tac.objects.create() 
        self.assertEquals(
            Tac.objects.count(),
            1
        ) 