# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from datetime import datetime, timezone
from farm.models import Customer
from farm.models.managers import CustomerEnum
from .tac import TacFactory #tac_id
class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    active_organization_id = Faker('random_int')
    email = Faker('email')
    email_confirmed_utc_date_time = Faker('date_time', tzinfo=timezone.utc)
    first_name = Faker('sentence', nb_words=4)
    forgot_password_key_expiration_utc_date_time = Faker('date_time', tzinfo=timezone.utc)
    forgot_password_key_value = Faker('sentence', nb_words=4)
    fs_user_code_value = factory.LazyFunction(uuid.uuid4)
    is_active = Faker('boolean')
    is_email_allowed = Faker('boolean')
    is_email_confirmed = Faker('boolean')
    is_email_marketing_allowed = Faker('boolean')
    is_locked = Faker('boolean')
    is_multiple_organizations_allowed = Faker('boolean')
    is_verbose_logging_forced = Faker('boolean')
    last_login_utc_date_time = Faker('date_time', tzinfo=timezone.utc)
    last_name = Faker('sentence', nb_words=4)
    password = Faker('sentence', nb_words=4)
    phone = Faker('phone_number')
    province = Faker('sentence', nb_words=4)
    registration_utc_date_time = Faker('date_time', tzinfo=timezone.utc)
    tac = SubFactory(TacFactory) #tac_id
    utc_offset_in_minutes = Faker('random_int')
    zip = Faker('sentence', nb_words=4)


 

