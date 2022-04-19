from django.contrib import admin
from achievements import models

admin.site.register(models.Achievement)
admin.site.register(models.Category)
admin.site.register(models.Tag)
