# factories.py

from factory import  Faker, SubFactory
from factory.django import DjangoModelFactory
from django.utils import timezone
import uuid
from api.models import ErrorLog 
from api.models.factories import PacFactory

class ErrorLogFactory(DjangoModelFactory):
    class Meta:
        model = ErrorLog

    code = Faker('uuid4')
    insert_utc_date_time = Faker('date_time_this_year', tzinfo=timezone.get_current_timezone())
    last_update_utc_date_time = Faker('date_time_this_year', tzinfo=timezone.get_current_timezone())
    insert_user_id = Faker('uuid4')
    last_update_user_id = Faker('uuid4')
    last_change_code = Faker('uuid4')
    browser_code = Faker('uuid4')
    context_code = Faker('uuid4')
    created_utc_date_time = Faker('date_time_this_year', tzinfo=timezone.get_current_timezone())
    description = Faker('text')
    is_client_side_error = Faker('boolean')
    is_resolved = Faker('boolean')
    pac = SubFactory(PacFactory) 
    url = Faker('url')
