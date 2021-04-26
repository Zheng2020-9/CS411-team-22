from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import CountySerializer
from .serializers import StateSerializer
from .models import County
from .models import State
from .models import UserProfile
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .forms import ProfileForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from django.template import RequestContext


#@csrf_exempt

# Create your views here.

class CountyView(viewsets.ViewSet):

    lookup_field = 'county_and_state'
    
    def list(self, request):
        queryset = County.objects.all()
        serializer = CountySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, county_and_state=None):
        queryset = County.objects.all()
        county = get_object_or_404(queryset, county_and_state=county_and_state)
        serializer = CountySerializer(county)
        return Response(serializer.data)   

    
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

def regist(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request, 'register.html',context)

def login(request):
    return render(request, 'login.html')


def profile(request):
    user = request.user
    return render(request, 'account/profile.html', {'user': user})


def profile_update(request):
    user = request.user
    user_profile = get_object_or_404(UserProfile, user=user)
 
    if request.method == "POST":
        form = ProfileForm(request.POST)
 
        if form.is_valid():
            
            user.first_name = form.cleaned_data['first_name'] 
            user.last_name = form.cleaned_data['last_name']
            user.save()
 
            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.save()
 
            return HttpResponseRedirect(reverse('todo:profile'))
    else:
        default_data = {'first_name': user.first_name, 'last_name': user.last_name, 'org': user_profile.org, 'telephone': user_profile.telephone, }
        form = ProfileForm(default_data)
 
    return render(request, 'account/profile_update.html', {'form': form, 'user': user})

    
