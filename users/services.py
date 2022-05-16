import requests
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

from dwi_backend.settings import BASE_SERVER_URL, ZONCORD_CLIENT_ID, ZONCORD_CLIENT_SECRET
from users.errors import IncorrectCode, CodeNotProvided, CodeOrRefreshTokenNotProvided


def get_profile_context(request) -> dict:
    """
    Gets information about the current user

    :param request:
    :return: user_id, user_url
    """
    context = {'url': f'http://{BASE_SERVER_URL}/users/user/{request.user.id}/'}
    return context


def get_user_data(access_token: str) -> dict:
    """
    A function that allows you to get user data from the main application using an access token

    :param access_token: Access token to the main application
    :return: first_name; last_name; profile_image
    """
    # Get user id
    url = f'{BASE_SERVER_URL}api/auth/user/'
    req = requests.get(url=url, headers={'Authorization': f'Bearer {access_token}'}).json()
    if 'error' in req:
        access_token = get_actual_token(token=access_token)
        req = requests.get(url=url, headers={'Authorization': f'Bearer {access_token}'}).json()
    user_id = req['pk']

    # get information about user
    url = f'{BASE_SERVER_URL}api/user_id/profile/{user_id}/'
    headers = {'Authorization': f'Bearer {access_token}'}
    user_data = requests.get(url=url, headers=headers).json()
    user_data['img'] = user_data['profile_photo']

    # return {'first_name': '123', 'last_name': '123', 'img': '123'}

    return user_data


def get_actual_token(token: str = None, code: str = None, refresh_token: str = None) -> str:
    """
    A function for updating the token and adding information about it to the database.

    :param token: Current or legacy access token
    :param code: Temporary token returned by the main application
    :param refresh_token: Access token recovery token
    :return: actual access token
    """
    if refresh_token is not None:
        token_data = get_token_data(refresh_token=refresh_token)

    if token is not None:
        user = get_user_model().objects.get(zoncord_access_token=token)
        refresh_token = user.zoncord_refresh_token
        token_data = get_token_data(refresh_token=refresh_token)

    if code is not None:
        token_data = get_token_data(code=code)

    if 'error' in token_data:
        raise IncorrectCode

    url = 'http://192.168.43.52:8001/api/auth/user/'
    headers = {'Authorization': f'Bearer {token_data["access_token"]}'}
    user_id = requests.get(url=url, headers=headers).json()['pk']

    user, created = get_user_model().objects.get_or_create(id=int(user_id))
    if created:
        user.username = str(user.id)
    user.zoncord_access_token = token_data['access_token']
    user.zoncord_refresh_token = token_data['refresh_token']
    user.save()

    return user.zoncord_access_token


def get_token_data(code: str = None, refresh_token: str = None) -> dict:
    """
    Authorization function in the main application

    :param refresh_token: Access token recovery token
    :param code: Temporary token returned by the main application
    :return: Data with access token to the main application
    """
    if code is not None:
        url = f'{BASE_SERVER_URL}o/token/'
        data = {
            'client_id': ZONCORD_CLIENT_ID,
            'client_secret': ZONCORD_CLIENT_SECRET,
            'code': code,
            'redirect_uri': 'http://192.168.43.76:8080/auth/',
            "grant_type": "authorization_code"
        }

        return requests.post(url=url, data=data).json()

    if refresh_token is not None:
        url = f'{BASE_SERVER_URL}o/token/'
        data = {
            'client_id': ZONCORD_CLIENT_ID,
            'client_secret': ZONCORD_CLIENT_SECRET,
            'refresh_token': refresh_token,
            'redirect_uri': 'http://192.168.43.76:8080/auth/',
            "grant_type": "refresh_token",
        }

        return requests.post(url=url, data=data).json()

    raise CodeOrRefreshTokenNotProvided()


def update_user_token(request) -> str:
    """
    Updates token information

    :param request:
    :return: access token
    """
    if 'code' not in request.data:
        raise CodeNotProvided

    code = request.data['code']

    token = get_actual_token(code=code)
    user = get_user_model().objects.get(zoncord_access_token=token)
    authorization_token = Token.objects.get_or_create(user=user)[0]

    return str(authorization_token)
