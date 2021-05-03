from rest_framework import serializers
from .models import County
from .models import State, UserProfile

class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('county_name', 'state', 'county_and_state', 'fips' , 'cases', 'deaths', 'vuln_score', 'avg_cases', 'avg_deaths')
        
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('name', 'fips', 'cases', 'deaths')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'org', 'telephone', 'mod_date', 'bookmarks')