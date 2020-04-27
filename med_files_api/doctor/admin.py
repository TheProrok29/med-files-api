from django.contrib import admin

from .models import Doctor, DoctorSpecialization


class DoctorAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'adres', 'phone_number', 'doc_spec']
    search_fields = ('name',)


class DoctorSpecializationAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['specialization', ]
    search_fields = ('specialization',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(DoctorSpecialization, DoctorSpecializationAdmin)
