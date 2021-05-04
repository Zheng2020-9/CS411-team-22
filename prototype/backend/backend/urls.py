"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from django.urls import path, include, re_path
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'States', views.StateView, 'State')
router.register(r'Counties', views.CountyView, 'County')
router.register(r'UserProfiles', views.UserProfileView, 'User Profiles')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
   # re_path(r'^accounts/', include('allauth.urls')),
   #URL for account
    path('accounts/', include('allauth.urls')),

    

    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),#change
    url(r"^", include("todo.urls")),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    
    
]
