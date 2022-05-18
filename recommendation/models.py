from django.db import models


class BasePreferred(models.Model):
    user = models.ForeignKey(verbose_name="user", to="users.User", on_delete=models.CASCADE)
    probability = models.FloatField(verbose_name="probability",
                                    help_text='the probability that the user likes the category')
    forecast_date_time = models.DateTimeField(verbose_name='date and time forecast',
                                              auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'base preferred'


class PreferredCategory(BasePreferred):
    category = models.ForeignKey(verbose_name="category", to="achievements.Category", on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.user} Category: {self.category} Probability: {self.probability}'

    class Meta:
        verbose_name = 'preferred category'
        verbose_name_plural = 'preferred categories'


class PreferredTag(BasePreferred):
    tag = models.ForeignKey(verbose_name="tag", to='achievements.Tag', related_name='tags', on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.user} Tag: {self.tag} Probability: {self.probability}'

    class Meta:
        verbose_name = 'preferred tag'
        verbose_name_plural = 'preferred tags'
