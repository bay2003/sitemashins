from django.db import models
from django.conf import settings
from usersapp.models import BlogUser
from rest_framework import routers, serializers, viewsets
from django.contrib import admin
from django.urls import path, include

class AcriveManager(models.Manager):
    def get_queryset(self):
        all_objects = super().get_queryset()
        return all_objects.filter(is_active=True)
class IsActiveMixin(models.Model):
    is_active = models.BooleanField(default=False)
    objects = models.Manager()
    active_objects = AcriveManager()
    class Meta:
        abstract = True

# class UpdatedObjectsManager(models.Manager):
#     def get_queryset(self):
#         all_objects = super().get_queryset()
#         return all_objects.filter(is_active=True)

class TimeStamp (models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', null=True, blank=True)
    # Другие поля, которые вам нужны
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(IsActiveMixin):
    objects = models.Manager()
    active_objects = AcriveManager()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @property
    def text(self):
        return self.name

from django.db import models
from django.urls import reverse

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)


    def get_absolute_url(self):
        return reverse('view_post', args=[str(self.id)])

    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)



class CoreObject(models.Model):
    name = models.CharField(max_length=32)

class Cer(CoreObject):
    description = models.TextField()

class Toy(CoreObject):
    text = models.TextField()


class Create(models.Model):
    objects = models.Manager()
    active_objects = AcriveManager()
    name = models.CharField(max_length=32, unique=True)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_posts')
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    user = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def has_image(self):
        return bool(self.image)

    def some_method(self):
        return "hello world"

