# Generated by Django 3.2.13 on 2022-05-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreferredCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField(help_text='the probability that the user likes the category', verbose_name='probability')),
                ('forecast_date_time', models.DateTimeField(auto_now=True, verbose_name='date and time forecast')),
            ],
            options={
                'verbose_name': 'preferred category',
                'verbose_name_plural': 'preferred categories',
            },
        ),
        migrations.CreateModel(
            name='PreferredTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probability', models.FloatField(help_text='the probability that the user likes the category', verbose_name='probability')),
                ('forecast_date_time', models.DateTimeField(auto_now=True, verbose_name='date and time forecast')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='achievements.tag', verbose_name='tag')),
            ],
            options={
                'verbose_name': 'preferred tag',
                'verbose_name_plural': 'preferred tags',
            },
        ),
    ]
