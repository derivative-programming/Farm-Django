from django.test import TestCase
from api.models import Pac 
from api.models.factories import PacFactory


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
        pac = PacFactory()
        self.assertTrue(isinstance(pac, Pac))
        self.assertIsNotNone(pac.code)
        self.assertIsNotNone(pac.insert_utc_date_time)
        self.assertIsNotNone(pac.last_update_utc_date_time)
        self.assertIsNotNone(pac.insert_user_id)
        self.assertIsNotNone(pac.last_update_user_id)
        self.assertIsNotNone(pac.last_change_code)
        self.assertIsNotNone(pac.description)
        self.assertIsNotNone(pac.display_order)
        self.assertIsNotNone(pac.is_active)
        self.assertIsNotNone(pac.lookup_enum_name)
        self.assertIsNotNone(pac.name)