from django import urls
from django.urls import path, include

from . import views
import api.views.fs_farm_api.v1_0 as api_views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from api import views  
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView

router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'tac-login',api_views.TacLoginViewSet,basename="tac-login")
router.register(r'tac-register',api_views.TacRegisterViewSet,basename="tac-register")
router.register(r'land-add-plant',api_views.LandAddPlantViewSet,basename="land-add-plant")
router.register(r'tac-farm-dashboard',api_views.TacFarmDashboardViewSet,basename="tac-farm-dashboard")
router.register(r'land-plant-list',api_views.LandPlantListViewSet,basename="land-plant-list")

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
 