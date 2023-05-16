from dataclasses import dataclass, asdict, field
from decimal import Decimal
from datetime import date, datetime
import json
import traceback
from dataclasses_json import dataclass_json,LetterCase, config
from typing import List
import uuid
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet,ViewSet
from rest_framework_dataclasses.serializers import DataclassSerializer
from rest_framework import status
from api.flows import FlowLandAddPlant,FlowLandAddPlantResult
from api.flows import FlowLandAddPlantInitObjWF,FlowLandAddPlantInitObjWFResult 
from api.flows import FlowValidationError
from api.models import Land
from dacite import from_dict
import marshmallow_dataclass
import logging
import marshmallow.exceptions 
from api.helpers import SessionContext
from api.helpers import TypeConversion

### response
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class ValidationError:
    property:str = ""
    message:str  = ""

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class PostResponse:
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandAddPlantPostResponse(PostResponse): 
    land_code:uuid = uuid.UUID(int=0) 
    plant_code:uuid = uuid.UUID(int=0)     
    output_flavor_code:uuid = uuid.UUID(int=0)    
    output_other_flavor:str = "" 
    output_some_int_val:int = 0 
    output_some_big_int_val:int = 0 
    output_some_bit_val:bool = False 
    output_is_edit_allowed:bool = False 
    output_is_delete_allowed:bool = False 
    output_some_float_val:float = 0
    output_some_decimal_val:Decimal = Decimal(0)
    output_some_utc_date_time_val:datetime = field(default_factory=TypeConversion.get_default_date_time, 
            metadata=config(
            encoder=datetime.isoformat, 
            decoder=datetime.fromisoformat
        )) 
    output_some_date_val:date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat, 
            decoder=date.fromisoformat
        ))
    output_some_money_val:Decimal = Decimal(0)
    output_some_n_var_char_val:str = "" 
    output_some_var_char_val:str = "" 
    output_some_text_val:str = "" 
    output_some_phone_number:str = "" 
    output_some_email_address:str = ""  

    def load_flow_response(self,data:FlowLandAddPlantResult): 
        self.land_code = data.land_code
        self.plant_code = data.land_code
        self.output_flavor_code = data.land_code  
        self.output_other_flavor = data.output_other_flavor
        self.output_some_int_val = data.output_some_int_val
        self.output_some_big_int_val = data.output_some_big_int_val 
        self.output_some_bit_val = data.output_some_bit_val
        self.output_is_edit_allowed = data.output_is_edit_allowed 
        self.output_is_delete_allowed = data.output_is_delete_allowed
        self.output_some_float_val = data.output_some_float_val
        self.output_some_decimal_val = data.output_some_decimal_val
        self.output_some_utc_date_time_val = data.output_some_utc_date_time_val
        self.output_some_date_val = data.output_some_date_val
        self.output_some_money_val = data.output_some_money_val
        self.output_some_n_var_char_val = data.output_some_n_var_char_val
        self.output_some_var_char_val = data.output_some_var_char_val
        self.output_some_text_val = data.output_some_text_val
        self.output_some_phone_number = data.output_some_phone_number
        self.output_some_email_address = data.output_some_email_address

### request. expect camel case. use marshmallow to validate.
@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class LandAddPlantPostModel:
    requestFlavorCode:uuid = uuid.UUID(int=0)  
    requestOtherFlavor:str = ""
    requestSomeIntVal:int = 0 
    requestSomeBigIntVal:int = 0 
    requestSomeBitVal:bool = False 
    requestIsEditAllowed:bool = False 
    requestIsDeleteAllowed:bool = False 
    requestSomeFloatVal:float = 0
    requestSomeDecimalVal:Decimal = Decimal(0)
    requestSomeUTCDateTimeVal:datetime = field(default_factory=TypeConversion.get_default_date_time, 
            metadata=config(
            encoder=datetime.isoformat, 
            decoder=datetime.fromisoformat
        )) 
    requestSomeDateVal:date = field(default_factory=TypeConversion.get_default_date, metadata=config(
            encoder=date.isoformat, 
            decoder=date.fromisoformat
        ))
    requestSomeMoneyVal:Decimal = Decimal(0)
    requestSomeNVarCharVal:str = ""
    requestSomeVarCharVal:str = ""
    requestSomeTextVal:str = ""
    requestSomePhoneNumber:str = ""
    requestSomeEmailAddress:str = ""
    requestSampleImageUploadFile:str = ""


### init response
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class GetInitResponse:
    success:bool = False
    message:str = ""
    validation_errors:List[ValidationError] = field(default_factory=list)

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LandAddPlantGetInitResponse(GetInitResponse):
    email:str = ""
    password:str = ""

    def load_flow_response(self,data:FlowLandAddPlantInitObjWFResult):
        self.email = data.email
        self.password = data.password
 
  


class LandAddPlantViewSet(ViewSet): 

    @action(detail=False, methods=['post'],url_path=r'(?P<landCode>[0-9a-f-]{36})')
    def submit(self, request, landCode=None, *args, **kwargs): 
        logging.debug('LandAddPlantViewSet.submit post start. landCode:' + landCode)

        response = LandAddPlantPostResponse()
         
        try:
            logging.debug("Start session...")
            session_context = SessionContext(dict())

            logging.debug("Request:" + json.dumps(request.data))

            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(LandAddPlantPostModel)()
             
            logging.debug("validating request...")
            request:LandAddPlantPostModel = schema.load(request.data)  

            logging.debug("loading model...")
            land = Land.objects.get(code=landCode)
            
            logging.debug("process flow...")
            flow = FlowLandAddPlant(session_context)
            flowResponse = flow.process(
                land,
                request.requestFlavorCode,
                request.requestOtherFlavor,
                request.requestSomeIntVal,    
                request.requestSomeBigIntVal,    
                request.requestSomeBitVal,    
                request.requestIsEditAllowed,    
                request.requestIsDeleteAllowed,    
                request.requestSomeFloatVal,    
                request.requestSomeDecimalVal,    
                request.requestSomeUTCDateTimeVal,
                request.requestSomeDateVal, 
                request.requestSomeMoneyVal,    
                request.requestSomeNVarCharVal,    
                request.requestSomeVarCharVal,    
                request.requestSomeTextVal,    
                request.requestSomePhoneNumber,    
                request.requestSomeEmailAddress,    
                request.requestSampleImageUploadFile,
            ) 

            response.load_flow_response(flowResponse);
            response.success = True
            response.message = "Success."

        except marshmallow.exceptions.ValidationError as se:
            response.success = False
            response.message = "Schema validation error. Invalid Request" 
             
        except TypeError as te: 
            response.success = False
            traceback_string = "".join(traceback.format_tb(te.__traceback__))
            response.message = str(te) + " traceback:" + traceback_string
            
        except FlowValidationError as ve:
            response.success = False 
            response.validation_errors = list()
            for key in ve.error_dict:
                response.validation_errors.append(ValidationError(key,ve.error_dict[key]))

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('LandAddPlantViewSet.submit get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 
    
    
    @action(detail=False, methods=['get'],url_path=r'(?P<landCode>[0-9a-f-]{36})/init')
    def init(self, request, landCode=None, *args, **kwargs):
        logging.debug('LandAddPlantViewSet.init get start. landCode:' + landCode)
        
        response = LandAddPlantGetInitResponse() 
         
        try: 
            logging.debug("Start session...")
            session_context = SessionContext(dict())
 
            logging.debug("loading model...")
            land = Land.objects.get(code=landCode)
            
            logging.debug("process flow...")
            flow = FlowLandAddPlantInitObjWF(session_context)
            flowResponse = flow.process(
                land
            ) 
 
            response.load_flow_response(flowResponse);
            response.success = True
            response.message = "Success."
            
        except TypeError as te: 
            response.success = False
            traceback_string = "Invalid Request" 
            
        except FlowValidationError as ve:
            response.success = False 
            response.validation_errors = list()
            for key in ve.error_dict:
                response.validation_errors.append(ValidationError(key,ve.error_dict[key]))

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('LandAddPlantViewSet.init get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 