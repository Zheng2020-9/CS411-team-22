from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CountySerializer
from .serializers import StateSerializer
from .models import County
from .models import State

# Create your views here.

class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
    
class StateView(viewsets.ViewSet):

    lookup_field = 'name'
    
    def list(self, request):
        queryset = State.objects.all()
        serializer = StateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, name=None):
        queryset = State.objects.all()
        state = get_object_or_404(queryset, name=name)
        serializer = StateSerializer(state)
        return Response(serializer.data)   