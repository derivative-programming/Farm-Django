import factory
import uuid
from django.utils import timezone
from factory import Faker, SubFactory
from faker import Factory as FakerFactory
from api.models import Customer
from faker import Faker
from datetime import timedelta 
from .Tac import TacFactory
 



class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
 
    active_organization_id = factory.Sequence(lambda n: n)
    email = factory.Faker('email')
    email_confirmed_utc_date_time = factory.Faker('past_datetime', start_date="-30d")
    first_name = factory.Sequence(lambda n: f"first_name{n}")
    forgot_password_key_expiration_utc_date_time = factory.Faker('past_datetime', start_date="-30d")
    forgot_password_key_value = factory.Sequence(lambda n: f"forgot_password_key_value{n}")
    fs_user_code_value = factory.Sequence(lambda n: f"{uuid.uuid4()}")
    is_active = True
    is_email_allowed = factory.Faker('boolean')
    is_email_confirmed = factory.Faker('boolean')
    is_email_marketing_allowed = factory.Faker('boolean')
    is_locked = False
    is_multiple_organizations_allowed = factory.Faker('boolean')
    is_verbose_logging_forced = factory.Faker('boolean')
    last_login_utc_date_time = factory.Faker('past_datetime', start_date="-30d")
    last_name = factory.Sequence(lambda n: f"last_name{n}")
    password = factory.Sequence(lambda n: f"password{n}")
    phone = factory.LazyAttribute(lambda n: f"{factory.Faker('phone_number')}")
    province = factory.Sequence(lambda n: f"province{n}")
    registration_utc_date_time = factory.Faker('past_datetime', start_date="-30d")
    tac = factory.SubFactory(TacFactory)
    utc_offset_in_minutes = factory.Sequence(lambda n: n)
    zip = factory.Sequence(lambda n: f"zip{n}")

    @factory.lazy_attribute
    def insert_user_id(self):
        return uuid.uuid4()

    @factory.lazy_attribute
    def last_update_user_id(self):
        return uuid.uuid4()