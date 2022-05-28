from django.contrib import admin

# Register your models here.
from rating.models import AchievementRating, PostRating, UserRating

admin.site.register(AchievementRating)
admin.site.register(PostRating)
admin.site.register(UserRating)
