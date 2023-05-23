from django import urls
from django.urls import path, include

from . import views
import api.views.fs_farm_api.v1_0 as api_views   #vrdebug
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from api import views  
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView

router = DefaultRouter() 
##GENLOOPApiSiteStart
##GENTrainingBlock[a]Start
##GENLearn[modelType=apiSite,name=FSFarmAPI]Start 
##GENLOOPApiEndPointStart
##GENTrainingBlock[b]Start
##GENLearn[modelType=apiEndPoint,name=LandAddPlant]Start 
router.register(r'land-add-plant',api_views.LandAddPlantViewSet,basename="land-add-plant")
##GENLearn[modelType=apiEndPoint,name=LandAddPlant]End
##GENTrainingBlock[b]End
##GENLOOPApiEndPointEnd
##GENLearn[modelType=apiSite,name=FSFarmAPI]End 
router.register(r'land-plant-list',api_views.LandPlantListViewSet,basename="land-plant-list")
router.register(r'tac-farm-dashboard',api_views.TacFarmDashboardViewSet,basename="tac-farm-dashboard")
router.register(r'tac-login',api_views.TacLoginViewSet,basename="tac-login")
router.register(r'tac-register',api_views.TacRegisterViewSet,basename="tac-register")
##GENTrainingBlock[a]End
##GENLOOPApiSiteEnd

urlpatterns = [ 
    path('', include(router.urls)),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'/static/json/openapi.json'}
    ), name='redoc'),
    path('swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'/static/json/openapi.json'}
    ), name='redoc'),
]
 