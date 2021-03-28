from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import CountySerializer
from .serializers import StateSerializer
from .models import County
from .models import State
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


@csrf_exempt

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

  



def search_view(request):

    return render(request,'test.html')

def handle(request):
    
    text = request.POST.get('sts')


    return HttpResponse(text)
    
