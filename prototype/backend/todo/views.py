from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializers import CountySerializer
from .serializers import StateSerializer, UserProfileSerializer
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
from .token import enctry, dectry
from django.conf import settings
from .forms import UserSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import ensure_csrf_cookie
#@csrf_exempt

# Create your views here.


@permission_classes([])
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

@permission_classes([])
class UserProfileView(viewsets.ViewSet):

    lookup_field = 'user'
    
    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, user=None):
        queryset = UserProfile.objects.all()
        county = get_object_or_404(queryset, user=user)
        serializer = UserSerializer(county)
        return Response(serializer.data)


# Create your views here.


# GITHUB ID AND SECRET
SOCIAL_AUTH_GITHUB_KEY = settings.SOCIAL_AUTH_GITHUB_KEY
SOCIAL_AUTH_GITHUB_SECRET = settings.SOCIAL_AUTH_GITHUB_SECRET

# OAUTH TOOLKIT ID AND SECRET
CLIENT_ID = 'lYiRF81KKZAhm18dq6hTuQFkY6l6tnZabsjrK9re'#settings.CLIENT_ID
CLIENT_SECRET = 'GlZNTPPLA4s2Ol8rR7VhAG1DnLIp2Bv5Je2Gqf4P7EG7ZIfCYAXcBMcQ238jPgg2qevNija5nHtrqyj1IWJycXJtBi6OdohbuolRu0kGh12vY2nLYTXJtlgrhvhnpxzv'  #settings.CLIENT_SECRET

client_id= "87AqIpPmm2CiRwHMd5QvNUnsrkDQHYyrTgV4EuDy",
client_secret= "tg0nm0F2G5oyICbyPL5tWvX0GWVAkBfFgMWW6yWuQ7gPrYMsg2wdMbpWnyZSvxvzNJZKwmt3MBNl3zoV5FoQdDUA9knfmrqR9ILQXPpKmaA4mjlaH0AaYc8lUXmBEz26",


@permission_classes([])   
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
    print(request)
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

@api_view(['POST'])
@permission_classes([])
def github_authenticate(request):
    github_token, Username, Userid = generate_github_access_token(
        github_client_id="0e04fc00c07db82338b0",
        github_client_secret="56d8708e74cb846b460d8d2298e71c4ecdbe8ed4",
        github_code=request.data['code']
    )

    django_auth_token = enctry(Username)#convert_to_auth_token(enctry(Username))
    user = get_user_from_token(django_auth_token)
    print("go return")

    return Response(
        {'token': django_auth_token,
         'user': Username},#UserSerializer(user).data
         status=status.HTTP_201_CREATED
    )

@api_view(['POST'])
@permission_classes([])
def user_operate(request):
    token = request.data['token']
    command = request.data['command']
    
    print("Command: " + command);
    print("Token: " + token);
    Userid = dectry(token)
    print("DecryToken: " + token);
    user = User.objects.get(username=Userid)
    print('User is: ' + str(user))
    
    user_profile = UserProfile.objects.get(user=user)
    
    #toAdd = '25025'
    #user_profile.add_bookmark(toAdd)
    #print(user_profile.get_bookmarks())

    #try:
    #    user = User.objects.get(username=Userid)
    #    print('is this working')
    #except User.DoesNotExist:
    #    HttpResponse('Access Denied')
    
    #user_profile = get_object_or_404(UserProfile, user=User)

    if command == 'addBM':
        Bookmark = request.data['BM']
        user_profile.add_bookmark(Bookmark)
    elif command == 'deleteBM':
        Bookmark = request.data['BM']
        user_profile.delete_bookmark(Bookmark)
    elif command == 'getBM':
        bookmarks = user_profile.get_bookmarks()
        return Response(
        {'BM': bookmarks}
        )
    else:
        HttpResponse('command error')
    return Response(
        {'result': 'success'}
        )
    
