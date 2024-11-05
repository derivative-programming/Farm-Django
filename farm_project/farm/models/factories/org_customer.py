# farm/models/factories.py
import uuid
import factory
import random
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from datetime import datetime, timezone
from farm.models import OrgCustomer
from farm.models.managers import OrgCustomerEnum
from .customer import CustomerFactory #customer_id
from .organization import OrganizationFactory #organization_id
class OrgCustomerFactory(DjangoModelFactory):
    class Meta:
        model = OrgCustomer
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    customer = SubFactory(CustomerFactory) #customer_id
    email = Faker('email')
    organization = SubFactory(OrganizationFactory) #organization_id


 

