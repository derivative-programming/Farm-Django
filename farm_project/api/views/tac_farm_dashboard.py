from dataclasses import dataclass, asdict, field
import json
from dataclasses_json import dataclass_json,LetterCase
import traceback
from typing import List
import uuid
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet,ViewSet
from rest_framework_dataclasses.serializers import DataclassSerializer
from rest_framework import status
from api.reports import ReportManagerTacFarmDashboard
from api.reports.row_models import ReportItemTacFarmDashboard
from api.flows import FlowTacFarmDashboardInitReport,FlowTacFarmDashboardInitReportResult
from api.flows import FlowValidationError
from api.models import Tac
from dacite import from_dict
import marshmallow_dataclass
import logging
import marshmallow.exceptions 
from api.reports import ReportRequestValidationError 
from api.helpers import SessionContext
from api.views.models import ListRequest, ListModel, ValidationError
from api.views.models.init import GetInitResponse
   


### request. expect camel case. use marshmallow to validate.
@dataclass_json(letter_case=LetterCase.SNAKE)
@dataclass
class TacFarmDashboardListRequest(ListRequest):
    pass 

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacFarmDashboardListModelItem():
    field_one_plant_list_link_land_code:uuid = uuid.UUID(int=0)

    def load_report_item(self,data:ReportItemTacFarmDashboard):
        self.field_one_plant_list_link_land_code = data.field_one_plant_list_link_land_code 


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacFarmDashboardListModel(ListModel):
    request:TacFarmDashboardListRequest = None
    items:List[TacFarmDashboardListModelItem] = field(default_factory=list)

@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class TacFarmDashboardGetInitResponse(GetInitResponse):
    customer_code:uuid = uuid.UUID(int=0)

    def load_flow_response(self,data:FlowTacFarmDashboardInitReportResult):
        self.customer_code = data.customer_code 
 

class TacFarmDashboardViewSet(ViewSet): 

    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})')
    def submit(self, request, tacCode=None, *args, **kwargs): 
        logging.debug('TacFarmDashboardViewSet.submit get start. tacCode:' + tacCode)

        response = TacFarmDashboardListModel()
         
        try:
            session_context = SessionContext(dict())

            logging.debug("Request:" + json.dumps(request.query_params))

            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(TacFarmDashboardListRequest)()
            
            logging.debug("validating request...")
            request = schema.load(request.query_params)  

            response.request = request

            logging.debug("loading model...")
            tac = Tac.objects.get(code=tacCode)
            
            logging.debug("generate report...")
            generator = ReportManagerTacFarmDashboard(session_context)
            items = generator.generate(
                    tacCode,
                    request.pageNumber,
                    request.itemCountPerPage,
                    request.orderByColumnName,
                    request.orderByDescending)

            response.items = list()

            for item in items:
                report_item = TacFarmDashboardListModelItem()
                report_item.load_report_item(item)
                response.items.append(report_item) 

            response.success = True
            response.message = "Success."

        except marshmallow.exceptions.ValidationError as se:
            response.success = False
            response.message = "Schema validation error. Invalid Request"  
            
        except ReportRequestValidationError as ve:
            response.success = False 
            response.validation_errors = list()
            for key in ve.error_dict:
                response.validation_errors.append(ValidationError(key,ve.error_dict[key]))
        

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('TacFarmDashboardViewSet.submit get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 
    
    
    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})/init')
    def init(self, request, tacCode=None, *args, **kwargs):
        logging.debug('TacFarmDashboardViewSet.init get start. tacCode:' + tacCode)
        
        response = TacFarmDashboardGetInitResponse() 
         
        try:
            session_context = SessionContext(dict())

            logging.debug("loading model...")
            tac = Tac.objects.get(code=tacCode)
            
            logging.debug("process flow...")
            flow = FlowTacFarmDashboardInitReport(session_context)
            flowResponse = flow.process(
                tac, 
            ) 
            
            response.load_flow_response(flowResponse);
            response.success = True
            response.message = "Success."
            
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
            
        logging.debug('TacFarmDashboardViewSet.init get result:' + response.to_json())
 
        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 