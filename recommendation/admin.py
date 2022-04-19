from django.contrib import admin

from recommendation import models

admin.site.register(models.PreferredCategory)
admin.site.register(models.PreferredTag)
