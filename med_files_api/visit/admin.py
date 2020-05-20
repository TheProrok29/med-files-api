from django.contrib import admin

from .models import Visit


class VisitAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'doctor', 'visit_date', 'user']
    search_fields = ('name', 'doctor')


admin.site.register(Visit, VisitAdmin)
