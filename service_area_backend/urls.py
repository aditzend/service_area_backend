from django.conf.urls import url, include


urlpatterns = [
    url('', include('providers.urls')),
]