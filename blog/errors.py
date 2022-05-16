from rest_framework.exceptions import APIException


class NotTheOwnerOfTheAchievement(APIException):
    status_code = 400
    default_detail = ('You are not the owner of the achievement.', )
