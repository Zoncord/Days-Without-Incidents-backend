# Generated by Django 3.2.13 on 2022-04-21 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='comment text', max_length=4096, verbose_name='text')),
                ('date_time_of_creation', models.DateTimeField(verbose_name='Date and time of creation')),
                ('date_time_of_last_edit', models.DateTimeField(verbose_name='Date and time of last edit')),
            ],
            options={
                'verbose_name': 'answer',
                'verbose_name_plural': 'answers',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='comment text', max_length=4096, verbose_name='text')),
                ('date_time_of_creation', models.DateTimeField(verbose_name='Date and time of creation')),
                ('date_time_of_last_edit', models.DateTimeField(verbose_name='Date and time of last edit')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.BooleanField(default=True, verbose_name='published')),
                ('slug', models.SlugField(max_length=256, verbose_name='slug')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('description', models.CharField(max_length=4096, verbose_name='description')),
                ('date_time_of_creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date and time of creation')),
                ('date_time_of_last_edit', models.DateTimeField(auto_now=True, null=True, verbose_name='Date and time of last edit')),
                ('achievement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='achievements.achievement', verbose_name='achievement')),
            ],
            options={
                'verbose_name': 'general information',
                'verbose_name_plural': 'generals information',
                'abstract': False,
            },
        ),
    ]