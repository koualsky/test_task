from django.contrib import admin

from address.models import Address, City

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
