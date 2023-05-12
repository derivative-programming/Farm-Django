from django.test import TestCase
from api.models import TriStateFilter 
 



class TriStateFilterTestCase(TestCase):
    def test_triStateFilter(self):
        self.assertEquals(
            TriStateFilter.objects.count(),
            0
        )
        TriStateFilter.objects.create() 
        self.assertEquals(
            TriStateFilter.objects.count(),
            1
        ) 