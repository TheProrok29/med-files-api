from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase

from ..models import Medicine


class MedicineModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@something.com',
            password='Testpassword123')

    def test_create_medicine_with_full_data(self):
        medicine = Medicine.objects.create(
            user=self.user,
            name='Gripex',
            description='This is the best pain killer',
            med_form=Medicine.MedicineForm.TABLETS,
            med_type=Medicine.MedicineType.PROBIOTIC,)
        self.assertTrue(isinstance(medicine, Medicine))
        self.assertEqual(medicine.__str__(), medicine.name)

    def test_create_medicine_with_minimum_data_and_default_value(self):
        expected_type = 'VIT'
        expected_form = 'TAB'
        medicine = Medicine.objects.create(user=self.user, name='Apap')
        self.assertEqual(medicine.med_type, expected_type)
        self.assertEqual(medicine.med_form, expected_form)

    def test_create_the_same_medicine_for_different_user_success(self):
        medicine1 = Medicine.objects.create(
            user=self.user,
            name='Gripex')
        user = get_user_model().objects.create_user(
            email='tom@gmail.com',
            password='Testpassword123')
        medicine2 = Medicine.objects.create(
            user=user,
            name='Gripex')
        self.assertEqual(Medicine.objects.all().count(), 2)
        self.assertEqual(medicine1.name, medicine2.name)

    def test_create_the_same_medicine_for_the_same_user_fails(self):
        Medicine.objects.create(
            user=self.user,
            name='Gripex')
        with self.assertRaises(Exception) as raised:
            Medicine.objects.create(
                user=self.user,
                name='Gripex')
        self.assertEqual(IntegrityError, type(raised.exception))
