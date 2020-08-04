from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


from address.models import Address, City


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
