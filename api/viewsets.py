from rest_framework import viewsets
from .import models
from .import serializers
class properties_2Views(viewsets.ModelViewSet):
    queryset=models.properties_2.objects.all()
    serializer_class=serializers.properties_2Serializer
    
    