from core.models import Tag
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone
from doctor.models import Doctor
from med_result.models import MedResult
from medicine.models import Medicine

from ..models import Visit


class VisitModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@something.com',
            password='Testpassword123')
        self.doctor = Doctor.objects.create(user=self.user, name='Jan Kowalski')
        self.medicine = Medicine.objects.create(user=self.user, name='Apap')
        self.tag = Tag.objects.create(user=self.user, name='Wro')
        self.med_result = MedResult.objects.create(user=self.user, name='Head Rentgen', date_of_exam=timezone.now())

    def test_create_visit_with_full_data(self):
        """Test creating a new visit"""
        visit = Visit.objects.create(user=self.user,
                                     visit_date=timezone.now(),
                                     name='Wizyta Laryngologiczna',
                                     address='Opole Chrobrego 24/3d',
                                     doctor=self.doctor)
        visit.medicine.add(self.medicine)
        visit.med_result.add(self.med_result)
        visit.tag.add(self.tag)
        self.assertTrue(isinstance(visit, Visit))
        self.assertEqual(visit.__str__(), visit.name)
        self.assertEqual(visit.tag.get(), self.tag)

    def test_create_visit_with_minimum_data(self):
        """Test creating a new visit with minimum data"""
        visit = Visit.objects.create(user=self.user,
                                     name='Wizyta Urologiczna',
                                     doctor=self.doctor)
        self.assertEqual(visit.name, 'Wizyta Urologiczna')
        self.assertEqual(visit.doctor, self.doctor)

    def test_create_visit_with_broken_data(self):
        """Test creating visit using broken data, based on database constraint
        must be fails"""
        with self.assertRaises(Exception) as raised1:
            Visit.objects.create(user=self.user,
                                 name='Wizyta Urologiczna',
                                 doctor='Pan Jan')
        with self.assertRaises(Exception) as raised2:
            Visit.objects.create(user=self.user,
                                 name=None,
                                 doctor=self.doctor)
        self.assertEqual(ValueError, type(raised1.exception))
        self.assertEqual(IntegrityError, type(raised2.exception))
