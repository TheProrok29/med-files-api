from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User, Tag


class UserAdmin(BaseUserAdmin):
    """Override UserAdmin class to use CRUD methods related to own user model in django admin"""
    ordering = ['id']
    list_display = ['email', 'name', 'born_date', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'born_date')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'name')


admin.site.register(User, UserAdmin)
admin.site.register(Tag)
