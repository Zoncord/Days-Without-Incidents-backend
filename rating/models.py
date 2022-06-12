from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import UniqueConstraint


class AchievementRating(models.Model):
    user = models.ForeignKey(to=get_user_model(), verbose_name='user', on_delete=models.CASCADE,
                             related_name='achievement_rating')
    achievement = models.ForeignKey(to='achievements.Achievement', verbose_name='achievement',
                                    on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return str(self.user) + ' ' + str(self.achievement)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'achievement'], name='achievement_rating_unique')
        ]
        verbose_name = 'achievement rating'
        verbose_name_plural = 'achievement ratings'


class PostRating(models.Model):
    user = models.ForeignKey(to=get_user_model(), verbose_name='user', on_delete=models.CASCADE,
                             related_name='post_rating')
    post = models.ForeignKey(to='blog.Post', verbose_name='post',
                             on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return str(self.user) + ' ' + str(self.post)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'post'], name='post_rating_unique')
        ]
        verbose_name = 'post rating'
        verbose_name_plural = 'post ratings'


class CommentRating(models.Model):
    user = models.ForeignKey(to=get_user_model(), verbose_name='user', on_delete=models.CASCADE,
                             related_name='comment_rating')
    comment = models.ForeignKey(to='blog.Comment', verbose_name='post',
                                on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return str(self.user) + ' ' + str(self.comment)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'comment'], name='comment_rating_unique')
        ]
        verbose_name = 'comment rating'
        verbose_name_plural = 'comments ratings'


class AnswerRating(models.Model):
    user = models.ForeignKey(to=get_user_model(), verbose_name='user', on_delete=models.CASCADE,
                             related_name='answer_rating')
    answer = models.ForeignKey(to='blog.Answer', verbose_name='post',
                               on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return str(self.user) + ' ' + str(self.answer)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'answer'], name='answer_rating_unique')
        ]
        verbose_name = 'answer rating'
        verbose_name_plural = 'answers ratings'


class UserRating(models.Model):
    user = models.ForeignKey(to=get_user_model(), verbose_name='user', on_delete=models.CASCADE,
                             related_name='user_rating')
    evaluated_user = models.ForeignKey(to=get_user_model(), verbose_name='estimated user',
                                       on_delete=models.CASCADE,
                                       related_name='ratings')

    def __str__(self):
        return str(self.user) + ' ' + str(self.evaluated_user)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'evaluated_user'], name='user_rating_unique')
        ]
        verbose_name = 'user rating'
        verbose_name_plural = 'users ratings'
