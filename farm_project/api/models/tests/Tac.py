from django.test import TestCase
from api.models import Tac 
from api.factories import TacFactory


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
        # create a TAC object with default attributes
        tac = TacFactory.create()
        # assert that the object was created successfully
        self.assertIsInstance(tac, Tac)
        self.assertIsNotNone(tac.code)
        self.assertIsNotNone(tac.insert_user_id)
        self.assertIsNotNone(tac.last_update_user_id)
        self.assertIsNotNone(tac.description)
        self.assertIsNotNone(tac.display_order)
        self.assertIsNotNone(tac.is_active)
        self.assertIsNotNone(tac.lookup_enum_name)
        self.assertIsNotNone(tac.name)
        self.assertIsNotNone(tac.pac)