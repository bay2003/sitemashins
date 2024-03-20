from django.conf.urls import url, include
from .models import Category, Post
from rest_framework import routers, serializers, viewsets


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        exclude = ['user']