from django.contrib import admin
from .models import Project, Create, Category, Tag, Page, Post
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Page)
admin.site.register(Post)

class CreateAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'created_at', 'updated_at', 'category', 'image')  # Отображаемые поля в админке

admin.site.register(Create, CreateAdmin)

