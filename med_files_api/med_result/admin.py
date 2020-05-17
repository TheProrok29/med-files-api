from django.contrib import admin

from .models import MedResult, MedImage


class MedResultAdmin(admin.ModelAdmin):
    model = MedResult
    ordering = ['id']
    list_display = ['name', 'user', 'add_date', 'med_image']
    search_fields = ('name', 'user')

    def med_image(self, obj):
        return MedImage.objects.filter(med_result=obj)


admin.site.register(MedResult, MedResultAdmin)
admin.site.register(MedImage)
