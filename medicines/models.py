from django.db import models
from django.utils.translation import gettext_lazy as _


class Medicines(models.Model):
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

    name = models.CharField(verbose_name='Name', max_length=120)
    description = models.TextField(verbose_name='Description')
    med_form = models.CharField(
        verbose_name='Form', max_length=3, choices=MedicineForm.choices, default=MedicineForm.TABLETS, )
    med_type = models.CharField(
        verbose_name='Type', max_length=3, choices=MedicineType.choices, default=MedicineType.VITAMIN, )
    when_added = models.DateTimeField(
        verbose_name='When added', auto_now_add=True)

    def __str__(self):
        return self.name
