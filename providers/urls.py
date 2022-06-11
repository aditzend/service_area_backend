from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from providers import views


router = DefaultRouter()
router.register('providers', views.ProviderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]