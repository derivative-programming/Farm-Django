from django.test import TestCase
from api.models import TriStateFilter 
from api.models.factories.TriStateFilter import TriStateFilterFactory


class TriStateFilterTestCase(TestCase):
    def setUp(self):
        TriStateFilter.objects.all().delete()

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
        # create a TriStateFilter object with default attributes
        triStateFilter = TriStateFilterFactory.create()
        # assert that the object was created successfully
        self.assertIsInstance(triStateFilter, TriStateFilter)
        self.assertIsNotNone(triStateFilter.code)
        self.assertIsNotNone(triStateFilter.insert_user_id)
        self.assertIsNotNone(triStateFilter.last_update_user_id)
        self.assertIsNotNone(triStateFilter.description)
        self.assertIsNotNone(triStateFilter.display_order)
        self.assertIsNotNone(triStateFilter.is_active)
        self.assertIsNotNone(triStateFilter.lookup_enum_name)
        self.assertIsNotNone(triStateFilter.name)
        self.assertIsNotNone(triStateFilter.pac)