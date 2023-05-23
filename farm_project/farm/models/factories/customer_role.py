# farm/models/factories.py
import uuid
import factory
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from farm.models import CustomerRole
from .customer import CustomerFactory #customer_id
from .role import RoleFactory #role_id
class CustomerRoleFactory(DjangoModelFactory):
    class Meta:
        model = CustomerRole
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(timezone.now)
    last_update_utc_date_time = factory.LazyFunction(timezone.now)
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    customer = SubFactory(CustomerFactory) #customer_id
    is_placeholder = Faker('boolean')
    placeholder = Faker('boolean')
    role = SubFactory(RoleFactory) #role_id
