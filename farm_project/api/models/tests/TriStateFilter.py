from django.test import TestCase
from api.models import TriStateFilter 
from api.models.factories.TriStateFilter import TriStateFilterFactory


class TriStateFilterTestCase(TestCase):
    def setUp(self): 
        self.tri_state_filter = TriStateFilterFactory.create()

    def test_tri_state_filter_creation(self):
        # Test that the instance was created
        self.assertIsNotNone(self.tri_state_filter)

    def test_tri_state_filter_fields(self): 
        self.assertIsInstance(self.tri_state_filter, TriStateFilter)
        self.assertIsNotNone(self.tri_state_filter.code)
        self.assertIsNotNone(self.tri_state_filter.insert_user_id)
        self.assertIsNotNone(self.tri_state_filter.last_update_user_id)
        self.assertIsNotNone(self.tri_state_filter.description)
        self.assertIsNotNone(self.tri_state_filter.display_order)
        self.assertIsNotNone(self.tri_state_filter.is_active)
        self.assertIsNotNone(self.tri_state_filter.lookup_enum_name)
        self.assertIsNotNone(self.tri_state_filter.name)
        self.assertIsNotNone(self.tri_state_filter.pac)