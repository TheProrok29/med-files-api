from medicine.models import Medicine
from rest_framework.test import APITestCase
from rest_framework import status

MEDICINE_URL = 'http://127.0.0.1:8000/api/medicine/'


class MedicinesApiTest(APITestCase):
    def test_medicines_get_method(self):
        response = self.client.get(MEDICINE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_medicines_post_method(self):
        data = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': Medicine.MedicineForm.GLOBULES,
            'med_type': Medicine.MedicineType.VITAMIN,
        }
        response = self.client.post(MEDICINE_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
