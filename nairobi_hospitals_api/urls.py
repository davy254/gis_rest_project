from  django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'nairobihealthfacilities', views.NairobiHealthFacilitiesViewSet)
router.register(r'nairobisubcounties', views.NairobiSubCountiesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

