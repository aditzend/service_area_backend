from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from providers.models import Provider
from providers.serializers import ProviderSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows providers to be viewed or edited.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    @action(detail=True)
    def get_provider_by_id(self, request, pk=None):
        """
        Get a provider by id.
        """
        provider = Provider.objects.get(pk=pk)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)
