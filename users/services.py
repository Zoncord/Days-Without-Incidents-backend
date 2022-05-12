from random import randint

import requests
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from dwi_backend.settings import BASE_SERVER_URL, ZONCORD_CLIENT_ID, ZONCORD_CLIENT_SECRET
from users.errors import IncorrectCode, CodeNotProvided


def get_user_data(access_token: str) -> dict:
    """
    A function that allows you to get user data from the main application using an access token

    :param access_token: Access token to the main application
    :return: first_name; last_name; profile_image
    """
    url = f'{BASE_SERVER_URL}auth/user/'
    # user_data = requests.get(url=url).json()
    return {'first_name': 'Kirill', 'last_name': 'Firsov', 'img': '123'}
    return user_data


def get_token_data(code: str) -> dict:
    url = f'{BASE_SERVER_URL}o/token/'
    data = {
        'client_id': ZONCORD_CLIENT_ID,
        'client_secret': ZONCORD_CLIENT_SECRET,
        'code': code,
        'redirect_uri': 'https://dwi.zoncord.tech/auth/',
        "grant_type": "authorization_code"
    }

    return requests.post(url=url, data=data).json()


def update_user_token(request) -> str:
    if 'code' not in request.data:
        raise CodeNotProvided

    code = request.data['code']

    token_data = get_token_data(code)

    if 'error' in token_data:
        raise IncorrectCode

    user = get_user_model().objects.get_or_create(id=int(token_data['pk']))[0]
    user.zoncord_access_token = token_data['token']
    user.save()

    authorization_token = Token.objects.get_or_create(user=user)[0]

    return authorization_token
