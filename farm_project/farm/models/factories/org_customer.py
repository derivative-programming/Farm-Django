# farm/models/factories.py
import uuid
import factory
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from farm.models import OrgCustomer
from .customer import CustomerFactory #customer_id
from .organization import OrganizationFactory #organization_id
class OrgCustomerFactory(DjangoModelFactory):
    class Meta:
        model = OrgCustomer
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    customer = SubFactory(CustomerFactory) #customer_id
    email = Faker('email')
    organization = SubFactory(OrganizationFactory) #organization_id
