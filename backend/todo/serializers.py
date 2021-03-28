from rest_framework import serializers
from .models import County
from .models import State

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'name', 'state_name', 'stats')
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'name', 'fips', 'cases', 'deaths')