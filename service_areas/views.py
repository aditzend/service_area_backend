from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from service_areas.models import ServiceArea
from service_areas.serializers import ServiceAreaSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows service areas to be viewed or edited.
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    @action(detail=True)
    def get_service_area_by_id(self, request, pk=None):
        """
        Get a service area by id.
        """
        service_area = ServiceArea.objects.get(pk=pk)
        serializer = ServiceAreaSerializer(service_area)
        return Response(serializer.data)
