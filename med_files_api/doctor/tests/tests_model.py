from django.test import TestCase
from ..models import Doctor, DoctorSpecialization
from django.contrib.auth import get_user_model


class DoctorSpecializationModelTest(TestCase):
    def test_create_new_spacialziation(self):
        """Test creating a new doctor specialization"""
        doc_specialization = DoctorSpecialization.objects.create(specialization='Neurologist')
        self.assertTrue(isinstance(doc_specialization, DoctorSpecialization))
        self.assertEqual(str(doc_specialization), 'Neurologist')


class DoctorModelTest(TestCase):
    def test_create_doctor_with_full_data(self):
        """Test creating a new doctor"""
        user = get_user_model().objects.create_user(
            email='test@something.com',
            password='Testpassword123')
        doc_spec = DoctorSpecialization.objects.create(specialization='Neurologist')
        doctor = Doctor.objects.create(user=user,
                                       name='Tom Hardy',
                                       adres='Warsaw, Chrobrego 25/4a',
                                       phone_number='765789432',
                                       doc_spec=doc_spec)
        self.assertTrue(isinstance(doctor, Doctor))
        self.assertEqual(doctor.__str__(), doctor.name)
