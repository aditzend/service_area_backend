from django.conf.urls import url, include


urlpatterns = [
    url('', include('providers.urls')),
    url('', include('service_areas.urls')),
]
