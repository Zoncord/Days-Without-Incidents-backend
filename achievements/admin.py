from django.contrib import admin
from achievements import models

admin.site.register(models.Achievement)


class IncidentAdmin(admin.ModelAdmin):
    fields = ('date_time', 'achievement')


admin.site.register(models.Incident)
admin.site.register(models.Category)
admin.site.register(models.Tag)
