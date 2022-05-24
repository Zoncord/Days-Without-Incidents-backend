import datetime
from django.db import models
from django.utils import timezone

from core.models import GeneralInformation, Published


class Achievement(GeneralInformation, Published):
    owners = models.ManyToManyField(verbose_name='achievement creators', to='users.User', related_name='achievements')
    main_achievement = models.ForeignKey(verbose_name='main achievement', to='achievements.Achievement',
                                         help_text='The achievement from which it was created. If unique, then black',
                                         on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(verbose_name='category', to='achievements.Category', related_name='achievements',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(verbose_name='tags', to="achievements.Tag", related_name='achievements', blank=True)
    likes = models.ManyToManyField(verbose_name='likes', help_text='users who liked', related_name='achievement_likes',
                                   to='users.User', blank=True)
    is_private = models.BooleanField('privacy', default=False)

    def __str__(self):
        return str(self.title)

    def days_since_the_last_incident(self):
        return (datetime.datetime.now() - self.incidents.last().date_time).days

    def likes_count(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'achievement'
        verbose_name_plural = 'achievements'


class Incident(models.Model):
    achievement = models.ForeignKey(Achievement, verbose_name='achievement', on_delete=models.CASCADE,
                                    related_name='incidents')
    date_time = models.DateTimeField(verbose_name="Date and time of incident", default=timezone.now)


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
