from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_author = models.BooleanField(default=False)  # Исправил опечатку в названии поля
    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)  # Вызываем сначала родительский метод сохранения
            if not Profile.objects.filter(user=self).exists():
                Profile.objects.get_or_create(user=self)  # Используем get_or_create для создания профиля пользователя


class Profile(models.Model):
    info = models.TextField(blank=True)
    user = models.OneToOneField(BlogUser, on_delete=models.CASCADE)

# @receiver(post_save, sender=BlogUser)
# def create_profile(sender, instance, **kwargs):
#     if not Profile.objects.filter(user=instance).exists():
#         Profile.objects.create(user=instance)