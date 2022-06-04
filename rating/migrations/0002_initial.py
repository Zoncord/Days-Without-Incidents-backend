# Generated by Django 3.2.13 on 2022-05-28 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('achievements', '0002_initial'),
        ('rating', '0001_initial'),
        ('blog', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userrating',
            name='evaluated_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL, verbose_name='Оцениваемый пользователь'),
        ),
        migrations.AddField(
            model_name='userrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='postrating',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='blog.post', verbose_name='пост'),
        ),
        migrations.AddField(
            model_name='postrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_rating', to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='achievementrating',
            name='achievement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='achievements.achievement', verbose_name='achievement'),
        ),
        migrations.AddField(
            model_name='achievementrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievement_rating', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddConstraint(
            model_name='userrating',
            constraint=models.UniqueConstraint(fields=('user', 'evaluated_user'), name='user_rating_unique'),
        ),
        migrations.AddConstraint(
            model_name='postrating',
            constraint=models.UniqueConstraint(fields=('user', 'post'), name='post_rating_unique'),
        ),
        migrations.AddConstraint(
            model_name='achievementrating',
            constraint=models.UniqueConstraint(fields=('user', 'achievement'), name='achievement_rating_unique'),
        ),
    ]
