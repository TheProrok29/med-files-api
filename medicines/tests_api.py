from rest_framework.test import APITestCase
from .models import Medicines


class MedicinesApiTest(APITestCase):
    def test_medicines_get_method(self):
        url = 'http://127.0.0.1:8000/api/medicines/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_medicines_post_method(self):
        url = 'http://127.0.0.1:8000/api/medicines/'
        data = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': Medicines.MedicineForm.GLOBULES,
            'med_type': Medicines.MedicineType.VITAMIN,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
