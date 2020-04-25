from django.test import TestCase
from ..models import Doctor


class DoctorModelTest(TestCase):
    def test_create_doctor_with_full_data(self):
        """Test creating a new doctor"""
        doctor = Doctor.objects.create(name='Tom Hardy',
                                       adres='Warsaw, Chrobrego 25/4a',
                                       phone_number='765789432',
                                       doc_spec=Doctor.DoctorSpecialization.SURGEON,)
        self.assertTrue(isinstance(doctor, Doctor))
        self.assertEqual(doctor.__str__(), doctor.name)

    def test_create_doctor_with_minimum_data(self):
        """Test creating a new doctor with minimum data; doc_type is mandatory
        but has default value set in model"""
        name = 'Ward Brankenmister'
        doctor = Doctor.objects.create(name=name)
        self.assertEqual(doctor.name, name)
