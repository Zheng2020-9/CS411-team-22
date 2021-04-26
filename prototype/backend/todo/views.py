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
from .oauth import generate_github_access_token, convert_to_auth_token, get_user_from_token

from django.conf import settings
from .forms import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

<<<<<<< HEAD
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

=======

# Create your views here.


# GITHUB ID AND SECRET
SOCIAL_AUTH_GITHUB_KEY = settings.SOCIAL_AUTH_GITHUB_KEY
SOCIAL_AUTH_GITHUB_SECRET = settings.SOCIAL_AUTH_GITHUB_SECRET

# OAUTH TOOLKIT ID AND SECRET
CLIENT_ID = settings.CLIENT_ID
CLIENT_SECRET = settings.CLIENT_SECRET




class CountyView(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    queryset = County.objects.all()
>>>>>>> Vivian
    
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


def github_authenticate(request):
    github_token = generate_github_access_token(
        github_client_id=SOCIAL_AUTH_GITHUB_KEY,
        github_client_secret=SOCIAL_AUTH_GITHUB_SECRET,
        github_code=request.data['code']
    )
    django_auth_token = convert_to_auth_token(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        backend='github',
        token=github_token
    )
    user = get_user_from_token(django_auth_token)

    return Response(
        {'token': django_auth_token,
         'user': UserSerializer(user).data},
        status=status.HTTP_201_CREATED
    )
    
