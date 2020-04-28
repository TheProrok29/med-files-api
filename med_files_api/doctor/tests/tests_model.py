from django.test import TestCase
from ..models import Doctor, DoctorSpecialization
from django.contrib.auth import get_user_model


class DoctorSpecializationModelTest(TestCase):
    def test_create_new_spacialziation(self):
        """Test creating a new doctor specialization"""
        specialization = DoctorSpecialization.objects.create(name='Neurologist')
        self.assertTrue(isinstance(specialization, DoctorSpecialization))
        self.assertEqual(str(specialization), 'Neurologist')


class DoctorModelTest(TestCase):
    def test_create_doctor(self):
        """Test creating a new doctor"""
        user = get_user_model().objects.create_user(
            email='test@something.com',
            password='Testpassword123')
        specialization = DoctorSpecialization.objects.create(name='Neurologist')
        doctor = Doctor.objects.create(user=user,
                                       name='Tom Hardy',
                                       adres='Warsaw, Chrobrego 25/4a',
                                       phone_number='765789432',
                                       specialization=specialization)
        self.assertTrue(isinstance(doctor, Doctor))
        self.assertEqual(doctor.__str__(), doctor.name)
