from django.test import TestCase

from ..models import Medicine


class MedicineModelTest(TestCase):

    def test_create_medicine_with_full_data(self):
        """Test creating a new medicine"""
        medicine = Medicine.objects.create(name='Gripex',
                                           description='This is the best pain killer',
                                           form=Medicine.MedicineForm.TABLETS,
                                           _type=Medicine.MedicineType.PROBIOTIC,)
        self.assertTrue(isinstance(medicine, Medicine))
        self.assertEqual(medicine.__str__(), medicine.name)

    def test_medicine_creation_with_minimum_data_and_default_value(self):
        """Test creating a new medicine with minimum data; med_type and med_form
        are mandatory but have default value set in model"""
        expected_type = 'VIT'
        expected_form = 'TAB'
        medicine = Medicine.objects.create(name='Apap')
        self.assertEqual(medicine.type, expected_type)
        self.assertEqual(medicine._form, expected_form)
