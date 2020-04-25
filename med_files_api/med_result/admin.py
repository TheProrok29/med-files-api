from django.contrib import admin

from .models import MedResult


class MedResultAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['user', 'add_date']
    search_fields = ('name',)


admin.site.register(MedResult, MedResultAdmin)
