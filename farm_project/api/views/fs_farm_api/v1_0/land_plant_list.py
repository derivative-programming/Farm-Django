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
from api.models import Land 
   
 
class LandPlantListViewSet(ViewSet): 
    isAPIAuthorizationRequired:bool = True
    isGetAvailable:bool = False
    isGetWithIdAvailable:bool = True
    isGetInitAvailable:bool = True
    isGetToCsvAvailable:bool = True
    isPostAvailable:bool = False
    isPostWithIdAvailable:bool = False
    isPutAvailable:bool = False 
    isDeleteAvailable:bool = False 
    # "apiGetInitContextTargetName": "CustomerUserLogOutInitObjWF",
    # "apiGetInitContextObjectName": "Customer",
    # "isGetToCsvAvailable": "false", 
    # "isPublic": "false",
    # "isLazyPost": "false", 
    # "pluralName": "customerUserLogOut",
    # "description": "CustomerUserLogOut Endpoint",
    # "apiCodeParamName": "CustomerCode",
    # "apiPostContextObjectName": "Customer",
    # "apiPostContextTargetName": "CustomerUserLogOut",
    # "isEndPointLoggingEnabled": "false",
    # "apiContextTargetName": "",
    # "apiContextObjectName": "",
    # "isGetContextCodeAParam": "false",

    @action(detail=False, methods=['get'],url_path=r'(?P<landCode>[0-9a-f-]{36})/init')
    def request_get_init(self, request, landCode=None, *args, **kwargs):
        logging.debug('LandPlantListViewSet.request_get_init start. landCode:' + landCode)
        if self.isGetInitAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
        
        response = view_init_models.LandPlantListInitReportGetInitModelResponse() 
         
        try: 
            logging.debug("Start session...")
            session_context = SessionContext(dict())
 
            logging.debug("loading model...")
            land = Land.objects.get(code=landCode)
            
            init_request = view_init_models.LandPlantListInitReportGetInitModelRequest()
            logging.debug("process request...") 
            response = init_request.process_request(
                session_context,
                land,
                response
            )  
            
        except TypeError as te: 
            response.success = False
            traceback_string = "".join(traceback.format_tb(te.__traceback__))
            response.message = str(te) + " traceback:" + traceback_string 

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('LandPlantListViewSet.init get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 
         
    @action(detail=False, methods=['get'])
    def request_get(self, request, landCode=None, *args, **kwargs):
        logging.debug('LandPlantListViewSet.request_get start.')
        if self.isGetAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 

    @action(detail=False, methods=['get'],url_path=r'(?P<landCode>[0-9a-f-]{36})')
    def request_get_with_id(self, request, landCode=None, *args, **kwargs): 
        logging.debug('LandPlantListViewSet.request_get_with_id start. landCode:' + landCode)
        if self.isGetWithIdAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 

        response = view_models.LandPlantListGetModelResponse()
         
        try:
            session_context = SessionContext(dict())

            logging.debug("Request:" + json.dumps(request.query_params))

            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(view_models.LandPlantListGetModelRequest)()
            
            logging.debug("validating request...")
            request = schema.load(request.query_params)  

            response.request = request

            logging.debug("loading model...")
            land = Land.objects.get(code=landCode)
            
            logging.debug("process request...") 
            response.process_request(
                session_context,
                land,
                request
            )  
            
        except marshmallow.exceptions.ValidationError as se:
            response.success = False
            response.message = "Schema validation error. Invalid Request"  
            

        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
 
        logging.debug('LandPlantListViewSet.submit get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 
  
    @action(detail=False, methods=['get'],url_path=r'(?P<landCode>[0-9a-f-]{36})/to-csv')
    def request_get_with_id_to_csv(self, request, landCode=None, *args, **kwargs):
        logging.debug('LandPlantListViewSet.request_get_with_id_to_csv start. landCode:' + landCode)
        if self.isGetToCsvAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 

        response = view_models.LandPlantListGetModelResponse()
         
        try:
            session_context = SessionContext(dict())

            logging.debug("Request:" + json.dumps(request.query_params))

            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(view_models.LandPlantListGetModelResponse)()
            
            logging.debug("validating request...")
            request = schema.load(request.query_params)  

            response.request = request

            logging.debug("loading model...")
            land = Land.objects.get(code=landCode)
            
            logging.debug("generate report...")
            generator = ReportManagerLandPlantList(session_context)
            items = generator.generate(
                    landCode,
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
  
    @action(detail=False, methods=['post'])
    def request_post(self, request, landCode=None, *args, **kwargs):
        logging.debug('LandPlantListViewSet.request_post start.')
        if self.isPostAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 

    @action(detail=False, methods=['post'],url_path=r'(?P<landCode>[0-9a-f-]{36})')
    def request_post_with_id(self, request, landCode=None, *args, **kwargs): 
        logging.debug('LandPlantListViewSet.request_post_with_id start. landCode:' + landCode)
        if self.isPostWithIdAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
        ##//GENTrainingBlock[casePostWithID]Start 
        ##//GENLearn[isPostWithIdAvailable=true]Start 
        ##//GENLearn[isPostWithIdAvailable=true]End 
        ##//GENTrainingBlock[casePostWithID]End 

    @action(detail=False, methods=['put'])
    def request_put(self, request, landCode=None, *args, **kwargs): 
        logging.debug('LandPlantListViewSet.request_put start.')
        if self.isPutAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 

    @action(detail=False, methods=['delete'])
    def request_delete(self, request, landCode=None, *args, **kwargs): 
        logging.debug('LandPlantListViewSet.request_delete start.')
        if self.isDeleteAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
    
         