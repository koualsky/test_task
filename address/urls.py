from rest_framework import routers

from address.views import AddressViewSet, CityViewSet


router = routers.SimpleRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'cities', CityViewSet)
urlpatterns = router.urls

