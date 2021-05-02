from rest_framework import serializers
from .models import County
from .models import State

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('county_name', 'state', 'county_and_state', 'fips' , 'cases', 'deaths', 'vuln_score')
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'fips', 'cases', 'deaths')