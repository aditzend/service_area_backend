from rest_framework import serializers
from service_areas.models import ServiceArea


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ['id', 'name', 'provider', 'price', 'geo_json_polygon']
