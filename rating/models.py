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
        verbose_name = 'оценка достижения'
        verbose_name_plural = 'оценки достижений'


class PostRating(models.Model):
    user = models.ForeignKey(to=get_user_model(), verbose_name='пользователь', on_delete=models.CASCADE,
                             related_name='post_rating')
    post = models.ForeignKey(to='blog.Post', verbose_name='пост',
                             on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return str(self.user) + ' ' + str(self.post)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'post'], name='post_rating_unique')
        ]
        verbose_name = 'оценка поста'
        verbose_name_plural = 'оценки постов'


class UserRating(models.Model):
    user = models.ForeignKey(to=get_user_model(), verbose_name='пользователь', on_delete=models.CASCADE,
                             related_name='user_rating')
    evaluated_user = models.ForeignKey(to=get_user_model(), verbose_name='Оцениваемый пользователь',
                                       on_delete=models.CASCADE,
                                       related_name='ratings')

    def __str__(self):
        return str(self.user) + ' ' + str(self.evaluated_user)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'evaluated_user'], name='user_rating_unique')
        ]
        verbose_name = 'оценка пользователя'
        verbose_name_plural = 'оценки пользователей'
