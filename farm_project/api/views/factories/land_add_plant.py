# api/models/factories.py
import uuid
import factory
from factory.django import DjangoModelFactory
from factory import Faker, SubFactory
from django.utils import timezone
from api.models import Plant
from api.models.factories import FlavorFactory #flavor_id
from api.models.factories import LandFactory #land_id
from api.views import LandAddPlantPostModel
from datetime import date, datetime
from decimal import Decimal

class LandAddPlantRequestFactory(factory.base.Factory):
    class Meta:
        model = LandAddPlantPostModel 
    requestFlavorCode:uuid = FlavorFactory.create().code  
    requestOtherFlavor:str = ""    
    requestSomeIntVal:int = Faker('random_int')    
    requestSomeBigIntVal:int = Faker('random_int') 
    requestSomeBitVal:bool = Faker('boolean')    
    requestIsEditAllowed:bool = Faker('boolean')    
    requestIsDeleteAllowed:bool = Faker('boolean')    
    requestSomeFloatVal:float = Faker('pyfloat', positive=True) 
    requestSomeDecimalVal:Decimal = Faker('pydecimal', left_digits=5, right_digits=2, positive=True) 
    requestSomeUTCDateTimeVal:datetime = Faker('date_time', tzinfo=timezone.utc)   
    requestSomeDateVal:date = Faker('date_object')    
    requestSomeMoneyVal:Decimal = Faker('pydecimal', left_digits=5, right_digits=2, positive=True)  
    requestSomeNVarCharVal:str = Faker('sentence', nb_words=4)    
    requestSomeVarCharVal:str = Faker('sentence', nb_words=4)    
    requestSomeTextVal:str = Faker('text')  
    requestSomePhoneNumber:str = Faker('phone_number')    
    requestSomeEmailAddress:str = Faker('email')    
    requestSampleImageUploadFile:str = ""

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default _create to use the dataclass's constructor."""
        return model_class(*args, **kwargs)