"""dwi_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core.views import main_redirect

schema_view = get_schema_view(
    openapi.Info(
        title="DWI API",
        default_version='v0.0.1',
        description="Open source social network where everyone can track people progress",
        contact=openapi.Contact(email="help@zoncord.tech"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('achievements/', include('achievements.urls'), name='achievements'),
    path('users/', include('users.urls'), name='users'),
    path('blog/', include('blog.urls'), name='blog'),
    path('rating/', include('rating.urls'), name='rating'),
    path('', main_redirect, name='main_redirect'),
    re_path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
