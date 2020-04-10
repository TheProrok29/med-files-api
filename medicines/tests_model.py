from django.test import TestCase
from .models import Medicine


class MedicinesModelCreateTest(TestCase):

    def test_medicine_creation(self):
        medicine = Medicine.objects.create(name='Gripex',
                                            description='This is the best pain killer',
                                            med_form=Medicine.MedicineForm.TABLETS,
                                            med_type=Medicine.MedicineType.PROBIOTIC,)
        self.assertTrue(isinstance(medicine, Medicine))
        self.assertEqual(medicine.__str__(), medicine.name)

    def test_medicine_creation_with_default_med_type(self):
        expected_med_type = 'VIT'
        medicine = Medicine.objects.create(name='Apap',
                                            description='This is a good things',
                                            med_form=Medicine.MedicineForm.TABLETS,)
        self.assertEqual(medicine.med_type, expected_med_type)

    def test_medicine_creation_with_default_med_form(self):
        expected_med_form = 'TAB'
        medicine = Medicine.objects.create(name='Something',
                                            description='Awesome',)
        self.assertEqual(medicine.med_form, expected_med_form)
