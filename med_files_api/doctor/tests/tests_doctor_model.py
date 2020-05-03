from django.test import TestCase
from ..models import Doctor
from django.contrib.auth import get_user_model


class DoctorModelTest(TestCase):
    def test_create_doctor(self):
        """Test creating a new doctor"""
        user = get_user_model().objects.create_user(
            email='test@something.com',
            password='Testpassword123')
        doctor = Doctor.objects.create(user=user,
                                       name='Tom Hardy',
                                       adres='Warsaw, Chrobrego 25/4a',
                                       phone_number='765789432',
                                       specialization=Doctor.DoctorSpecialization.SURGEON)
        self.assertTrue(isinstance(doctor, Doctor))
        self.assertEqual(doctor.__str__(), doctor.name)
