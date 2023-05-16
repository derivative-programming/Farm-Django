import json
import traceback 
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet 
from rest_framework import status
from api.flows import FlowLandAddPlant
from api.flows import FlowLandAddPlantInitObjWF 
from api.flows import FlowValidationError
from api.models import Land 
import marshmallow_dataclass
import logging
import marshmallow.exceptions 
from api.helpers import SessionContext 
import api.views.models as view_models
import api.views.models.init as view_init_models
 

class LandAddPlantViewSet(ViewSet): 

    @action(detail=False, methods=['post'],url_path=r'(?P<landCode>[0-9a-f-]{36})')
    def submit(self, request, landCode=None, *args, **kwargs): 
        logging.debug('LandAddPlantViewSet.submit post start. landCode:' + landCode)

        response = view_models.LandAddPlantPostResponse()
         
        try:
            logging.debug("Start session...")
            session_context = SessionContext(dict())


            logging.debug("Request:" + json.dumps(request.data)) 
 
            logging.debug("get schema")
            schema = marshmallow_dataclass.class_schema(view_models.LandAddPlantPostModel)() 
             
            logging.debug("validating request...")
            request:view_models.LandAddPlantPostModel = schema.load(request.data)  

            logging.debug("loading model...")
            land = Land.objects.get(code=landCode)
            
            logging.debug("process flow...")
            flowResponse = request.process_request(
                session_context,
                land,
                response
            )
            
            response.success = True
            response.message = "Success."

        except marshmallow.exceptions.ValidationError as se:
            response.success = False
            response.message = "Schema validation error. Invalid Request: " + str(se.messages)
             
        except TypeError as te: 
            response.success = False
            traceback_string = "".join(traceback.format_tb(te.__traceback__))
            response.message = str(te) + " traceback:" + traceback_string
             
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
        
        response = view_init_models.LandAddPlantGetInitResponse() 
         
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
 
        logging.debug('LandAddPlantViewSet.init get result:' + response.to_json())

        responseDict = json.loads(response.to_json())
        
        return Response(responseDict,status=status.HTTP_200_OK) 