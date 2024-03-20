from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Create, Post

@receiver(post_save, sender=Create)
def create_post_from_create(sender, instance, created, **kwargs):
    if created and instance.image:
        Post.objects.create(
            title=instance.name,
            content=instance.text,
            page=instance.category.page,
            image=instance.image
        )
