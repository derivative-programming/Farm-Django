# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from farm.models import OrgApiKey
from farm.models.managers import OrgApiKeyEnum
from .organization import OrganizationFactory #organization_id
from .org_customer import OrgCustomerFactory #org_customer_id
class OrgApiKeyFactory(DjangoModelFactory):
    class Meta:
        model = OrgApiKey
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    api_key_value = Faker('sentence', nb_words=4)
    created_by = Faker('sentence', nb_words=4)
    created_utc_date_time = Faker('date_time', tzinfo=timezone.utc)
    expiration_utc_date_time = Faker('date_time', tzinfo=timezone.utc)
    is_active = Faker('boolean')
    is_temp_user_key = Faker('boolean')
    name = Faker('sentence', nb_words=4)
    organization = SubFactory(OrganizationFactory) #organization_id
    org_customer = SubFactory(OrgCustomerFactory) #org_customer_id


 

