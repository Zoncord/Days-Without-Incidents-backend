from django.contrib import admin
from achievements import models

admin.site.register(models.Achievement)


class IncidentAdmin(admin.ModelAdmin):
    fields = ('date_time', )


admin.site.register(models.Incident, IncidentAdmin)
admin.site.register(models.Category)
admin.site.register(models.Tag)
