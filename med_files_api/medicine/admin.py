from django.contrib import admin

from .models import Medicine


class MedicineAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', '_type', 'form']
    search_fields = ('name',)


admin.site.register(Medicine, MedicineAdmin)
