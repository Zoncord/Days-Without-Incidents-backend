from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from core.models import Slug, GeneralInformation
from users.services import get_user_data


class User(AbstractUser, Slug):
    zoncord_access_token = models.CharField(verbose_name='access token', max_length=1024,
                                            help_text='access token to the main application', default=None, null=True,
                                            blank=True)
    zoncord_refresh_token = models.CharField(verbose_name='access token', max_length=1024,
                                             help_text='refresh token to the main application', default=None, null=True,
                                             blank=True)
    state = models.ForeignKey(verbose_name='user state', to='users.State', related_name='users',
                              on_delete=models.SET_NULL, null=True, blank=True)
    preferred_categories = models.ManyToManyField(verbose_name='preferred categories',
                                                  help_text='categories that a user might like',
                                                  to='achievements.Category', blank=True)
    description = models.CharField(verbose_name='description', max_length=4096, default='', blank=True)

    def followers_count(self):
        return self.ratings.count()

    def general_user_information(self):
        return get_user_data(self.zoncord_access_token)

    def __str__(self):
        return get_user_data(self.zoncord_access_token)['first_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class State(GeneralInformation):
    issued_by = models.ForeignKey(verbose_name='issued by', help_text="who issued the status", to='users.User',
                                  on_delete=models.SET_NULL, related_name="issued_states", null=True)
    expiration_date_time = models.DateTimeField(verbose_name="date and time when the user's status will change",
                                                help_text='if zero then time is unlimited')

    def __str__(self):
        return self.title
