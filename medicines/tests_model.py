from django.test import TestCase
from .models import Medicines


class MedicinesModelCreateTest(TestCase):

    def test_medicine_creation(self):
        medicine = Medicines.objects.create(name='Gripex',
                                            description='This is the best pain killer',
                                            med_form=Medicines.MedicineForm.TABLETS,
                                            med_type=Medicines.MedicineType.PROBIOTIC,)
        self.assertTrue(isinstance(medicine, Medicines))
        self.assertEqual(medicine.__str__(), medicine.name)

    def test_medicine_creation_with_default_med_type(self):
        expected_med_type = 'VIT'
        medicine = Medicines.objects.create(name='Apap',
                                            description='This is a good things',
                                            med_form=Medicines.MedicineForm.TABLETS,)
        self.assertEqual(medicine.med_type, expected_med_type)

    def test_medicine_creation_with_default_med_form(self):
        expected_med_form = 'TAB'
        medicine = Medicines.objects.create(name='Something',
                                            description='Awesome',)
        self.assertEqual(medicine.med_form, expected_med_form)
