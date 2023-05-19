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
from api.reports import ReportManagerLandPlantList
from api.reports.row_models import ReportItemLandPlantList
from api.flows import FlowLandPlantListInitReport,FlowLandPlantListInitReportResult
from api.flows import FlowValidationError
from api.models import Tac
from dacite import from_dict
import marshmallow_dataclass
import logging
import marshmallow.exceptions 
from api.reports import ReportRequestValidationError 
from api.helpers import SessionContext 
import api.views.models as view_models
import api.views.models.init as view_init_models
   
 
class LandPlantListViewSet(ViewSet): 

    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})')
    def submit(self, request, tacCode=None, *args, **kwargs): 
        logging.debug('LandPlantListViewSet.submit get start. tacCode:' + tacCode)

        response = view_models.LandPlantListListModel()
         
        try:
            session_context = SessionContext(dict())

            logging.debug("Request:" + json.dumps(request.query_params))

            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(view_models.LandPlantListListRequest)()
            
            logging.debug("validating request...")
            request = schema.load(request.query_params)  

            response.request = request

            logging.debug("loading model...")
            tac = Tac.objects.get(code=tacCode)
            
            logging.debug("generate report...")
            generator = ReportManagerLandPlantList(session_context)
            items = generator.generate(
                    tacCode,
                    request.pageNumber,
                    request.itemCountPerPage,
                    request.orderByColumnName,
                    request.orderByDescending)

            response.items = list()

            for item in items:
                report_item = view_models.LandPlantListListModelItem()
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
                response.validation_errors.append(view_models.ValidationError(key,ve.error_dict[key]))
        

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('LandPlantListViewSet.submit get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 
    
    
    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})/init')
    def init(self, request, tacCode=None, *args, **kwargs):
        logging.debug('LandPlantListViewSet.init get start. tacCode:' + tacCode)
        
        response = view_init_models.LandPlantListGetInitResponse() 
         
        try:
            session_context = SessionContext(dict())

            logging.debug("loading model...")
            tac = Tac.objects.get(code=tacCode)
            
            logging.debug("process flow...")
            flow = FlowLandPlantListInitReport(session_context)
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
                response.validation_errors.append(view_models.ValidationError(key,ve.error_dict[key]))

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
            
        logging.debug('LandPlantListViewSet.init get result:' + response.to_json())
 
        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 