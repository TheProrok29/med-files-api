from medicine.models import Medicine
from rest_framework.test import APITestCase
from rest_framework import status

MEDICINE_URL = 'http://127.0.0.1:8000/api/medicine/'


def create_medicine(**params):
    return Medicine.objects.create(**params)


class MedicinesApiTest(APITestCase):
    """Test the medicine API"""

    def test_medicine_endpoint_available(self):
        """Test  medicine endpoint is available"""
        response = self.client.get(MEDICINE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_medicine_with_full_data_success(self):
        """Test createing medicine with valid payload is successful"""
        payload = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': Medicine.MedicineForm.GLOBULES,
            'med_type': Medicine.MedicineType.VITAMIN,
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        medicine = Medicine.objects.get(**res.data)
        self.assertTrue(medicine.name, payload['name'])

    def test_create_medicine_with_min_data_success(self):
        """Test createing medicine with valid min payload is successful"""
        payload = {
            'name': 'New one',
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        medicine = Medicine.objects.get(**res.data)
        self.assertTrue(medicine.name, payload['name'])

    def test_medicine_exists(self):
        """Test creating medicine that already exists fails"""
        payload = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': Medicine.MedicineForm.GLOBULES,
            'med_type': Medicine.MedicineType.VITAMIN,
        }
        create_medicine(**payload)
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_medicine_invalid_med_form_fail(self):
        """"Test creating medicine with broken payload(med_form) must fail"""
        payload = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': 'Something',
            'med_type': Medicine.MedicineType.VITAMIN,
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_medicine_invalid_med_type_fail(self):
        """Test creating medicine with broken payload(med_type) must fail"""
        payload = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': Medicine.MedicineForm.GLOBULES,
            'med_type': 'Something',
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
