# Generated by Django 3.2.13 on 2022-06-08 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
    ]
