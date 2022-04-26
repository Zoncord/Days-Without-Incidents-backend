import datetime
from datetime import timezone

from django.db import models
from core.models import GeneralInformation, Published


class Achievement(GeneralInformation, Published):
    owners = models.ManyToManyField(verbose_name='achievement creators', to='users.User')
    main_achievement = models.ForeignKey(verbose_name='main achievement', to='achievements.Achievement',
                                         help_text='The achievement from which it was created. If unique, then black',
                                         on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(verbose_name='category', to='achievements.Category', related_name='achievements',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(verbose_name='tags', to="achievements.Tag", related_name='achievements', blank=True)
    likes = models.ManyToManyField(verbose_name='likes', help_text='users who liked', related_name='achievement_likes',
                                   to='users.User', blank=True)
    is_private = models.BooleanField('privacy', default=False)
    incidents = models.ManyToManyField(verbose_name='incidents', to='achievements.Incident', blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'achievement'
        verbose_name_plural = 'achievements'


class Incident(models.Model):
    date_time = models.DateTimeField(verbose_name="Date and time of incident", default=datetime.datetime.now())


class Category(GeneralInformation):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category'


class Tag(GeneralInformation):
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
