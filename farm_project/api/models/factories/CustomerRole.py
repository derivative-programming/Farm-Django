from datetime import timezone
from factory import SubFactory, Faker 
from factory.django import DjangoModelFactory
from api.models import CustomerRole, Customer, Role

class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer
    # Fill in any required fields here

class RoleFactory(DjangoModelFactory):
    class Meta:
        model = Role
    # Fill in any required fields here


class CustomerRoleFactory(DjangoModelFactory):
    class Meta:
        model = CustomerRole
    
    # code = Faker('uuid4')
    insert_utc_date_time = Faker('past_datetime', start_date="-30d")
    last_update_utc_date_time = Faker('past_datetime', start_date="-30d")
    insert_user_id = Faker('uuid4')
    last_update_user_id = Faker('uuid4')
    last_change_code = Faker('uuid4')
    customer = SubFactory(CustomerFactory)
    is_placeholder = Faker('boolean')
    placeholder = Faker('boolean')
    role = SubFactory(RoleFactory)