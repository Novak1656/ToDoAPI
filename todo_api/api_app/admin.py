from django.contrib import admin
from .models import User, Category, Task


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'tg_id', 'created_at']
    list_display_links = ['id', 'username']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'user', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
