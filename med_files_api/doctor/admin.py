from django.contrib import admin

from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'adres', 'phone_number', 'specialization']
    search_fields = ('name',)


admin.site.register(Doctor, DoctorAdmin)
