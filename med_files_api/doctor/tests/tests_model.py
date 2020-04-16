from django.test import TestCase
from doctor.models import Doctor


class DoctorModelTest(TestCase):
    def test_doctor_creation(self):
        doctor = Doctor.objects.create(name='Tom Hardy',
                                       adres='Warsaw, Chrobrego 25/4a',
                                       phone_number='765789432',
                                       doc_type=Doctor.DoctorSpecialization.SURGEON,)
        self.assertTrue(isinstance(doctor, Doctor))
        self.assertEqual(doctor.__str__(), doctor.name)
