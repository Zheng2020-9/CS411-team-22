# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:32:05 2021

@author: zsq1999
"""
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import UserProfile
from rest_framework.serializers import ModelSerializer



#class OrderForm(ModelForm):
  #  class Meta:
  #     model = Order
    #    fields = '__all__'



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username','first_name', 'last_name', 'email',
            'last_login', 'date_joined','token'
        )





class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
        
        
        

class ProfileForm(forms.Form):
 
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    org = forms.CharField(label='Organization', max_length=50, required=False)
    telephone = forms.CharField(label='Telephone', max_length=50, required=False)
 
 
class SignupForm(forms.Form):
 
    def signup(self, request, user):
        user_profile = UserProfile()
        user_profile.user = user
        user.save()
        user_profile.save()

