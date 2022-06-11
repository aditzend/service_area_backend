from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from service_areas import views


router = DefaultRouter()
router.register('service_areas', views.ServiceAreaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
