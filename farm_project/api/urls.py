from django import urls
from django.urls import path, include

from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from api import views  
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView

router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'tac-login',views.TacLoginViewSet,basename="tac-login")
router.register(r'tac-register',views.TacRegisterViewSet,basename="tac-register")
router.register(r'land-add-plant',views.LandAddPlantViewSet,basename="land-add-plant")
router.register(r'tac-farm-dashboard',views.TacFarmDashboardViewSet,basename="tac-farm-dashboard")

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
 