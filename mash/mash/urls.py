"""
URL configuration for mash project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from mash.mashapp.api_views import CategoryViewSet, PostViewSet
import rest_framework
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mashapp.urls')),
    path('users/', include('usersapp.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls')),
    path('category-detail/', include(router.urls)), path('api/v0/', include(router.urls)), # Поправил путь для категорий
]



