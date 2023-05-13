import factory
import uuid
from django.utils import timezone
from factory import Faker, SubFactory
from faker import Factory as FakerFactory
from .models import Pac, Tac, Customer
from faker import Faker
from datetime import timedelta
faker = FakerFactory.create()

class PacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pac

    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_udpate_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    description = factory.Faker('text', max_nb_chars=500)
    display_order = factory.Sequence(lambda n: n)
    is_active = factory.Faker('boolean')
    lookup_enum_name = factory.Faker('text', max_nb_chars=50)
    name = factory.Faker('text', max_nb_chars=100)

    @classmethod
    def create_batch(cls, size, **kwargs):
        return [cls() for _ in range(size)]


class TacFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tac

    tac_id = factory.Sequence(lambda n: n)
    code = uuid.uuid4()
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_udpate_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = uuid.uuid4()
    last_update_user_id = uuid.uuid4()
    last_change_code = uuid.uuid4()
    description = factory.Faker('text', max_nb_chars=500)
    display_order = factory.Sequence(lambda n: n)
    is_active = True
    lookup_enum_name = factory.Faker('word')
    name = factory.Faker('word')
    pac = SubFactory(PacFactory)


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    active_organization_id = factory.Sequence(lambda n: n)
    email = factory.LazyAttribute(lambda x: f"{faker.email()}")
    email_confirmed_utc_date_time = factory.LazyAttribute(lambda x: faker.date_time_this_year())
    first_name = factory.Sequence(lambda n: f"first_name{n}")
    forgot_password_key_expiration_utc_date_time = factory.LazyAttribute(lambda x: faker.date_time_this_year())
    forgot_password_key_value = factory.Sequence(lambda n: f"forgot_password_key_value{n}")
    fs_user_code_value = factory.Sequence(lambda n: f"{uuid.uuid4()}")
    is_active = True
    is_email_allowed = True
    is_email_confirmed = True
    is_email_marketing_allowed = True
    is_locked = False
    is_multiple_organizations_allowed = True
    is_verbose_logging_forced = False
    last_login_utc_date_time = factory.LazyAttribute(lambda x: faker.date_time_this_year())
    last_name = factory.Sequence(lambda n: f"last_name{n}")
    password = factory.Sequence(lambda n: f"password{n}")
    phone = factory.Sequence(lambda n: f"{faker.phone_number()}")
    province = factory.Sequence(lambda n: f"province{n}")
    registration_utc_date_time = factory.LazyAttribute(lambda x: faker.date_time_this_year())
    tac = factory.SubFactory(TacFactory)
    utc_offset_in_minutes = factory.Sequence(lambda n: n)
    zip = factory.Sequence(lambda n: f"zip{n}")

    @factory.lazy_attribute
    def insert_user_id(self):
        return uuid.uuid4()

    @factory.lazy_attribute
    def last_update_user_id(self):
        return uuid.uuid4()