from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    """Override UserAdmin class to use own ordering and field display"""
    ordering = ['id']
    list_display = ['name', 'email']


admin.site.register(User, UserAdmin)
