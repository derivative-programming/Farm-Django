# farm/models/factories.py
"""
This module initializes and imports the plant factory used in the project.
"""
import uuid
import random
from datetime import datetime, timezone
import factory
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from farm.models import Plant
from farm.models.managers import PlantEnum
from .flavor import FlavorFactory #flvr_foreign_key_id
from .land import LandFactory #land_id
class PlantFactory(DjangoModelFactory):
    """
    This class initializes the plant factory used in the project.
    """
    class Meta:
        """
        This class sets the model and the corresponding
        enum for the plant factory.
        """
        model = Plant
    code = factory.LazyFunction(uuid.uuid4)
    insert_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    last_update_utc_date_time = factory.LazyFunction(lambda: datetime.now(timezone.utc))
    insert_user_id = factory.LazyFunction(uuid.uuid4)
    last_update_user_id = factory.LazyFunction(uuid.uuid4)
    last_change_code = factory.LazyFunction(uuid.uuid4)
    flvr_foreign_key = SubFactory(FlavorFactory) #flvr_foreign_key_id  # type: ignore
    is_delete_allowed: bool = Faker('boolean') # type: ignore
    is_edit_allowed: bool = Faker('boolean') # type: ignore
    land = SubFactory(LandFactory) #land_id # type: ignore
    other_flavor: str = Faker('sentence', nb_words=4) # type: ignore
    some_big_int_val = Faker('random_int') # type: ignore
    some_bit_val: bool = Faker('boolean') # type: ignore
    some_date_val = Faker('date_object') # type: ignore
    some_decimal_val = Faker('pydecimal', left_digits=5, right_digits=2, positive=True) # type: ignore
    some_email_address: str = Faker('email') # type: ignore
    some_float_val = Faker('pyfloat', positive=True) # type: ignore
    some_int_val = Faker('random_int') # type: ignore
    some_money_val = Faker('pydecimal', left_digits=5, right_digits=2, positive=True) # type: ignore
    some_n_var_char_val = Faker('sentence', nb_words=4) # type: ignore
    some_phone_number: str = Faker('phone_number') # type: ignore
    some_text_val: str = Faker('text') # type: ignore
    some_uniqueidentifier_val = factory.LazyFunction(uuid.uuid4)
    some_utc_date_time_val: str = Faker('date_time', tzinfo=timezone.utc) # type: ignore
    some_var_char_val: str = Faker('sentence', nb_words=4) # type: ignore

##GENTrainingBlock[caselookup]Start
##GENLearn[isLookup=false,calculatedIsParentObjectAvailable=true]Start
##GENLearn[isLookup=false,calculatedIsParentObjectAvailable=true]End
##GENTrainingBlock[caselookup]End
