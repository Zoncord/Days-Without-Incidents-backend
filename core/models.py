from django.db import models
from django.utils import timezone


class Published(models.Model):
    is_published = models.BooleanField(verbose_name='published', default=True)

    class Meta:
        abstract = True
        verbose_name = 'condition'
        verbose_name_plural = 'conditions'


class Slug(models.Model):
    slug = models.SlugField(verbose_name='slug', max_length=256)

    class Meta(Published.Meta):
        abstract = True
        verbose_name = 'subdirectory'
        verbose_name_plural = 'subdirectories'


class GeneralInformation(Slug):
    title = models.CharField(verbose_name='title', max_length=256)
    description = models.CharField(verbose_name="description", max_length=4096)
    date_time_of_creation = models.DateTimeField(verbose_name="Date and time of creation", default=timezone.now)
    date_time_of_last_edit = models.DateTimeField(verbose_name="Date and time of last edit", default=timezone.now)

    def __str__(self):
        return self.title

    class Meta(Published.Meta):
        abstract = True
        verbose_name = 'general information'
        verbose_name_plural = 'generals information'
