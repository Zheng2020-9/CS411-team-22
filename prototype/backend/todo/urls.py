from django.urls import re_path
from . import views
from django.conf.urls import url


app_name = "todo"
urlpatterns = [
    url(r"^githubverify/$", views.github_authenticate, name='github-authenticate'),
    url(r"^useroperate/$", views.user_operate, name='userchange')
]

