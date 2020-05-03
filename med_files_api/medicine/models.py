from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Medicine(models.Model):
    class MedicineForm(models.TextChoices):
        TABLETS = 'TAB', _('Tablets')
        SYRUP = 'SYR', _('Surup')
        DROPS = 'DRO', _('Drops')
        OINTMENT = 'OIN', _('Ointment')
        GLOBULES = 'GLO', _('Globules')

    class MedicineType(models.TextChoices):
        ANTIBIOTIC = 'ANT', _('Antybiotic')
        PROBIOTIC = 'PRO', _('Probiotic')
        VITAMIN = 'VIT', _('Vitamin')
        SUPLEMENT = 'SUP', _('Suplement')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Name', max_length=120)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    form = models.CharField(
        verbose_name='Form', max_length=3, choices=MedicineForm.choices, default=MedicineForm.TABLETS, )
    _type = models.CharField(
        verbose_name='Type', max_length=3, choices=MedicineType.choices, default=MedicineType.VITAMIN, )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='medicine per user')
        ]

    def __str__(self):
        return self.name
