from django.contrib import admin
from .models import Project, Create, Category, Tag, Page, Post

def set_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
set_active.short_description = "Активировать выбранные посты"

class CreateAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'category', 'image', 'has_image', 'is_active']
    actions = ['clear_rating', set_active]
    # Отображаемые поля в админке

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Create, CreateAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    actions = [set_active]

admin.site.register(Tag, TagAdmin)
