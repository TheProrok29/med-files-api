from django.test import TestCase
from ..models import Doctor
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError


class DoctorModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@something.com',
            password='Testpassword123')

    def test_create_doctor_with_full_data(self):
        """Test creating a new doctor with all field filled"""
        doctor = Doctor.objects.create(user=self.user,
                                       name='Tom Hardy',
                                       adres='Warsaw, Chrobrego 25/4a',
                                       phone_number='765789432',
                                       specialization=Doctor.DoctorSpecialization.SURGEON)
        self.assertTrue(isinstance(doctor, Doctor))
        self.assertEqual(doctor.__str__(), doctor.name)

    def test_create_doctor_with_minimum_data_and_default_value(self):
        """Test creating a new doctor with minimum data; adres and phone field will
        be ampty and specialziation will be default family doctor"""
        doctor = Doctor.objects.create(user=self.user,
                                       name='Tom Hardy')
        self.assertTrue(isinstance(doctor, Doctor))
        self.assertEqual(doctor.__str__(), doctor.name)
        self.assertEqual(doctor.specialization, Doctor.DoctorSpecialization.FAMILY_DOCTOR)

    def test_create_the_same_doctor_for_different_user_success(self):
        """Test creating the same doctor for different user based on database constraint
        must be success"""
        doctor1 = Doctor.objects.create(user=self.user, name='Tom Hardy')
        user = get_user_model().objects.create_user(
            email='tom@gmail.com',
            password='Testpassword123')
        doctor2 = Doctor.objects.create(user=user, name='Tom Hardy')
        self.assertEqual(Doctor.objects.all().count(), 2)
        self.assertEqual(doctor1.name, doctor2.name)

    def test_create_the_same_doctor_for_the_same_user_fails(self):
        """Test creating the same doctor for the same user based on database constraint
        must be fails"""
        Doctor.objects.create(user=self.user, name='Tom Hardy')
        with self.assertRaises(Exception) as raised:
            Doctor.objects.create(user=self.user, name='Tom Hardy')
        self.assertEqual(IntegrityError, type(raised.exception))
