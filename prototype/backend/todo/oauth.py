import re 
import requests
import json

from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken

def generate_github_access_token(github_client_id, github_client_secret,github_code):
    """
    create an access token to github Oauth2.
    :param github_client_id: client_id from https://github.com/settings/developers
    :param github_client_secret: client_secret from https://github.com/settings/developers
    :param code: code generated by client from http://github.com/login/oauth/authorize/
     :return: json data on user's api
    """
    auth_response = requests.post(
    'https://github.com/login/oauth/access_token/',
    data=json.dumps({
    'client_id': github_client_id,
    'client_secret': github_client_secret,
    'code': github_code
    }),
    headers={'content-type': 'application/json'}
    )
    token= re.search(r"access_token=([a-zA-Z0-9]+)", auth_response.content.decode('utf-8'))
    if token is None:
        raise PermissionError(auth_response)
    return token.group(1)

def convert_to_auth_token(client_id, client_secret, backend, token):
    """
    given a previously generated access_token use the django-rest-framework-social-oauth2
    endpoint `/convert-token/` to authenticate the user and return a django auth token
    :param client_id: from OauthToolkit application
    :param client_secret: from OauthToolkit application
    :param backend: authentication backend to user ('github', 'facebook', etc)
    :param token: access token generated from the backend - github
    :return: django auth token
    """
    params = {
    'grant_type': 'convert_token',
    'client_id': client_id,
    'client_secret': client_secret,
    'backend': backend,
    'token': token,
    }
    response = requests.post('http://127.0.0.1:8000/auth/convert-token/', params=params)
    return response.json()

def get_user_from_token(django_auth_token):
    """
    Retrieve the user object given an access token
    :param django_auth_token: Oauthtoolkit access TOKEN
    :return: user object
    """
    return User.objects.get(
    id=AccessToken.objects.get(token=django_auth_token['access_token']).user_id)