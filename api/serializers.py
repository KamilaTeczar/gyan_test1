from rest_framework import serializers
from .models import properties_2
class properties_2Serializer(serializers.ModelSerializer):
    class Meta:
        model=properties_2
        fields='__all__'
