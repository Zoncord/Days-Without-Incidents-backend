def get_user_data(access_token: str) -> dict:
    """
    A function that allows you to get user data from the main application using an access token

    :param access_token: Access token to the main application
    :return: first_name; last_name; profile_image
    """
    return {'first_name': 'Kirill', 'last_name': 'Firsov', 'profile_image': '/img/'}
