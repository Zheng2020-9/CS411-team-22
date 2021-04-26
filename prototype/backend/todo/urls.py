from django.urls import re_path
from . import views
from django.conf.urls import url


app_name = "todo"
urlpatterns = [
    re_path(r'^profile/$', views.profile, name='profile'),
    re_path(r'^profile/update/$', views.profile_update, name='profile_update'),

]

