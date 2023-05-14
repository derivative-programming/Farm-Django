# api/models/factories.py

import uuid
import factory
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from api.models import Plant, Flavor, Land
from api.models.factories import FlavorFactory
from api.models.factories import LandFactory

class PlantFactory(DjangoModelFactory):
    class Meta:
        model = Plant

    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    flavor = SubFactory(FlavorFactory)
    is_delete_allowed = Faker('boolean')
    is_edit_allowed = Faker('boolean')
    land = SubFactory(LandFactory)
    other_flavor = Faker('sentence', nb_words=4)
    some_big_int_val = Faker('random_int')
    some_bit_val = Faker('boolean')
    some_date_val = Faker('date_object')
    some_decimal_val = Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    some_email_address = Faker('email')
    some_float_val = Faker('pyfloat', positive=True)
    some_int_val = Faker('random_int')
    some_money_val = Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    some_n_var_char_val = Faker('sentence', nb_words=4)
    some_phone_number = Faker('phone_number')
    some_text_val = Faker('text')
    some_uniqueidentifier_val = factory.LazyFunction(uuid.uuid4)
    some_utc_date_time_val = Faker('date_time', tzinfo=timezone.utc)
    some_var_char_val = Faker('sentence', nb_words=4)
