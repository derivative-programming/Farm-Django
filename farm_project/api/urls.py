from django import urls
from django.urls import path, include

from . import views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from api.views import TacLogin
from api.views import TacRegister
from api.views import TacFarmDashboard
from api.views import index
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView

router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet,basename="snippet")
router.register(r'tac-login',TacLogin.TacLoginViewSet,basename="tac-login")
router.register(r'tac-register',TacRegister.TacRegisterViewSet,basename="tac-register")
router.register(r'tac-farm-dashboard',TacFarmDashboard.TacFarmDashboardViewSet,basename="tac-farm-dashboard")

urlpatterns = [
    path("", index.index, name="index"), 
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
 