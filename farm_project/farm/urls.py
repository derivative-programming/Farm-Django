from django import urls
from django.urls import path, include

from . import views
import farm.views.fs_farm_api.v1_0 as api_views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from farm import views  
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
router.register(r'v1_0/land-add-plant',api_views.LandAddPlantViewSet,basename="v1_0/land-add-plant")
##GENLearn[modelType=apiEndPoint,name=LandAddPlant]End
##GENTrainingBlock[b]End
##GENLOOPApiEndPointEnd
##GENLearn[modelType=apiSite,name=FSFarmAPI]End 
router.register(r'v1_0/land-plant-list',api_views.LandPlantListViewSet,basename="v1_0/land-plant-list")
router.register(r'v1_0/tac-farm-dashboard',api_views.TacFarmDashboardViewSet,basename="v1_0/tac-farm-dashboard")
router.register(r'v1_0/tac-login',api_views.TacLoginViewSet,basename="v1_0/tac-login")
router.register(r'v1_0/tac-register',api_views.TacRegisterViewSet,basename="v1_0/tac-register")
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
 