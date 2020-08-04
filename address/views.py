from rest_framework import viewsets

from address.serializers import AddressSerializer, CitySerializer
from address.models import Address, City


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
