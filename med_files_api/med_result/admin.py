from django.contrib import admin

from .models import MedResult, MedImage


class MedResultAdmin(admin.ModelAdmin):
    model = MedResult
    ordering = ['id']
    list_display = ['name', 'user', 'add_date', 'med_image']
    search_fields = ('name', 'user')

    def med_image(self, obj):
        """
        Show all med images connected to concrete med result instance in django admin.
        """
        med_result = MedResult.objects.get(id=obj.id)
        return med_result.images.all()


admin.site.register(MedResult, MedResultAdmin)
admin.site.register(MedImage)
