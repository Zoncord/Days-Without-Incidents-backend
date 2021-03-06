from django.db import models
from django.utils import timezone

from core.models import GeneralInformation, Published


class Post(GeneralInformation, Published):
    author = models.ForeignKey(verbose_name='author', to='users.User', on_delete=models.SET_NULL, null=True)
    achievement = models.ForeignKey(verbose_name='achievement', to='achievements.Achievement',
                                    on_delete=models.CASCADE, null=True, related_name='posts')

    def likes_count(self):
        return self.ratings.count()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    author = models.ForeignKey(verbose_name='user', help_text='the user who left the comment', to='users.User',
                               on_delete=models.CASCADE)
    parent_comment = models.ForeignKey(verbose_name='comment', to='blog.Comment', related_name='answers',
                                       on_delete=models.CASCADE, blank=True, null=True, default=None)

    post = models.ForeignKey(verbose_name='post', help_text='post commented on', to='blog.Post',
                             on_delete=models.CASCADE, blank=True, null=True, default=None)
    text = models.CharField(verbose_name='text', help_text='comment text', max_length=4096)
    date_time_of_creation = models.DateTimeField(verbose_name="Date and time of creation", default=timezone.now)
    date_time_of_last_edit = models.DateTimeField(verbose_name="Date and time of last edit", default=timezone.now)

    def __str__(self):
        return str(self.author)

    def likes_count(self):
        return self.ratings.count()

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
