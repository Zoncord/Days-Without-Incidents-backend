from django.db import models
from core.models import GeneralInformation, Published


class Post(GeneralInformation, Published):
    author = models.ForeignKey(verbose_name='author', to='users.User', on_delete=models.SET_NULL, null=True)
    achievement = models.ForeignKey(verbose_name='achievement', to='achievements.Achievement',
                                    on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.title)


class BaseInformation(models.Model):
    user = models.ForeignKey(verbose_name='user', help_text='the user who left the comment', to='users.User',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='post', help_text='post commented on', to='blog.Post',
                             on_delete=models.CASCADE)
    text = models.CharField(verbose_name='text', help_text='comment text', max_length=4096)
    date_time_of_creation = models.DateTimeField(verbose_name="Date and time of creation")
    date_time_of_last_edit = models.DateTimeField(verbose_name="Date and time of last edit")

    def __str__(self):
        return str(self.user)

    class Meta:
        abstract = True
        verbose_name = 'base information'


class Comment(BaseInformation):
    likes = models.ManyToManyField(verbose_name='likes', help_text='users who liked', related_name='comment_likes',
                                   to='users.User')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Answers(BaseInformation):
    comment = models.ForeignKey(verbose_name='comment', to='blog.Comment', related_name='answers',
                                on_delete=models.CASCADE)
    likes = models.ManyToManyField(verbose_name='likes', help_text='users who liked', related_name='answer_likes',
                                   to='users.User')

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'
