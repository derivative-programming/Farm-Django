import json 
import traceback 
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet 
from rest_framework import status 
import marshmallow_dataclass
import logging
import marshmallow.exceptions  
from api.helpers import SessionContext 
import api.views.models as view_models
import api.views.models.init as view_init_models 
class TacFarmDashboardViewSet(ViewSet): 
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
    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})/init')
    def request_get_init(self, request, tacCode=None, *args, **kwargs):
        logging.debug('TacFarmDashboardViewSet.request_get_init start. tacCode:' + tacCode)
        if self.isGetInitAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
## 
        response = view_init_models.TacFarmDashboardInitReportGetInitModelResponse() 
        try: 
            logging.debug("Start session...")
            session_context = SessionContext(dict())
            init_request = view_init_models.TacFarmDashboardInitReportGetInitModelRequest() 
            response = init_request.process_request(
                session_context,
                tacCode,
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
        logging.debug('TacFarmDashboardViewSet.init get result:' + response.to_json())
        responseDict = json.loads(response.to_json())
        return Response(responseDict,status=status.HTTP_200_OK) 
## 
    @action(detail=False, methods=['get'])
    def request_get(self, request, tacCode=None, *args, **kwargs):
        logging.debug('TacFarmDashboardViewSet.request_get start.')
        if self.isGetAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
## 
    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})')
    def request_get_with_id(self, request, tacCode=None, *args, **kwargs): 
        logging.debug('TacFarmDashboardViewSet.request_get_with_id start. tacCode:' + tacCode)
        if self.isGetWithIdAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
## 
        response = view_models.TacFarmDashboardGetModelResponse()
        try:
            session_context = SessionContext(dict())
            logging.debug("Request:" + json.dumps(request.query_params))
            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(view_models.TacFarmDashboardGetModelRequest)()
            logging.debug("validating request...")
            request = schema.load(request.query_params)  
            response.request = request
            logging.debug("process request...") 
            response.process_request(
                session_context,
                tacCode,
                request
            )  
        except marshmallow.exceptions.ValidationError as se:
            response.success = False
            response.message = "Schema validation error. Invalid Request"  
        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
        logging.debug('TacFarmDashboardViewSet.submit get result:' + response.to_json())
        responseDict = json.loads(response.to_json())
        return Response(responseDict,status=status.HTTP_200_OK) 
## 
    @action(detail=False, methods=['get'],url_path=r'(?P<tacCode>[0-9a-f-]{36})/to-csv')
    def request_get_with_id_to_csv(self, request, tacCode=None, *args, **kwargs):
        logging.debug('TacFarmDashboardViewSet.request_get_with_id_to_csv start. tacCode:' + tacCode)
        if self.isGetToCsvAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
## 
        response = view_models.TacFarmDashboardGetModelResponse()
        try:
            session_context = SessionContext(dict())
            logging.debug("Request:" + json.dumps(request.query_params))
            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(view_models.TacFarmDashboardGetModelResponse)()
            logging.debug("validating request...")
            request = schema.load(request.query_params)  
            response.request = request
            logging.debug("process request...") 
            response.process_request(
                session_context,
                tacCode,
                request
            )  
        except marshmallow.exceptions.ValidationError as se:
            response.success = False
            response.message = "Schema validation error. Invalid Request"  
        except Exception as e:
            response.success = False
            traceback_string = "".join(traceback.format_tb(e.__traceback__))
            response.message = str(e) + " traceback:" + traceback_string
        logging.debug('TacFarmDashboardViewSet.submit get result:' + response.to_json())
        responseDict = json.loads(response.to_json())
        return Response(responseDict,status=status.HTTP_200_OK) 
## 
    @action(detail=False, methods=['post'])
    def request_post(self, request, tacCode=None, *args, **kwargs):
        logging.debug('TacFarmDashboardViewSet.request_post start.')
        if self.isPostAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
        ## 
    @action(detail=False, methods=['post'],url_path=r'(?P<tacCode>[0-9a-f-]{36})')
    def request_post_with_id(self, request, tacCode=None, *args, **kwargs): 
        logging.debug('TacFarmDashboardViewSet.request_post_with_id start. tacCode:' + tacCode)
        if self.isPostWithIdAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
        ## 
    @action(detail=False, methods=['put'])
    def request_put(self, request, tacCode=None, *args, **kwargs): 
        logging.debug('TacFarmDashboardViewSet.request_put start.')
        if self.isPutAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
        ## 
    @action(detail=False, methods=['delete'])
    def request_delete(self, request, tacCode=None, *args, **kwargs): 
        logging.debug('TacFarmDashboardViewSet.request_delete start.')
        if self.isDeleteAvailable == False:
            return Response(status=status.HTTP_501_NOT_IMPLEMENTED) 
        ## 
