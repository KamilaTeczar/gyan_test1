from api.viewsets import  properties_2Views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('properties_2',properties_2Views)