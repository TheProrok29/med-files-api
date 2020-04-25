from django.urls import reverse
from ..models import Doctor
from rest_framework import status
from rest_framework.test import APITestCase

DOCTOR_URL = reverse('api:doctor-list')


def create_doctor(**params):
    return Doctor.objects.create(**params)


class DoctorApiTest(APITestCase):
    """Test the doctor API"""

    def test_doctor_endpoint_available(self):
        """Test  doctor endpoint is available"""
        response = self.client.get(DOCTOR_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_doctor_with_full_data_success(self):
        """Test createing doctor with valid payload is successful"""
        payload = {
            'name': 'Fakren Makrewn',
            'adres': 'Opole 24/b',
            'phone_number': '456789086',
            'doc_spec': Doctor.DoctorSpecialization.ALLERGIST,
        }
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        doctor = Doctor.objects.get(**res.data)
        self.assertTrue(doctor.name, payload['name'])

    def test_create_doctor_with_min_data_success(self):
        """Test createing doctor with valid min payload is successful"""
        payload = {
            'name': 'Fakren Makrewn',
        }
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        doctor = Doctor.objects.get(**res.data)
        self.assertTrue(doctor.name, payload['name'])

    def test_doctor_exists(self):
        """Test creating doctor that already exists fails"""
        payload = {
            'name': 'Fakren Makrewn',
            'adres': 'Opole 24/b',
            'phone_number': '456789086',
            'doc_spec': Doctor.DoctorSpecialization.ALLERGIST,
        }
        create_doctor(**payload)
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_doctor_invalid_doc_spec_fail(self):
        """"Test creating doctor with broken payload(doc_spec) must fail"""
        payload = {
            'name': 'Fakren Makrewn',
            'adres': 'Opole 24/b',
            'phone_number': '456789086',
            'doc_spec': 'Something',
        }
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
