from django.contrib import admin
from .models import BlogUser
class CreateAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'created_at', 'updated_at', 'category', 'image')  # Отображаемые поля в админке

admin.site.register(BlogUser)

# Register your models here.
