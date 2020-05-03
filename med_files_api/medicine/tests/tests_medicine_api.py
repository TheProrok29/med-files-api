from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ..models import Medicine

MEDICINE_URL = reverse('api:medicine-list')


def create_medicine(**params):
    return Medicine.objects.create(**params)


class PublicMecicineApiTest(APITestCase):
    """Test the public medicine API endpoint"""

    def test_medicine_endpoint_available(self):
        """Test  medicine endpoint is available"""
        res = self.client.get(MEDICINE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMedicineApiTest(APITestCase):
    """Test the private medicine API endpoints"""

    def setUp(self):
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)

    def test_create_medicine_with_full_data_success(self):
        """Test createing medicine with valid payload is successful"""
        payload = {
            'user': self.user,
            'name': 'Gripex',
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
            'user': self.user,
            'name': 'Apap',
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        medicine = Medicine.objects.get(**res.data)
        self.assertTrue(medicine.name, payload['name'])

    def test_medicine_exists(self):
        """Test creating medicine that already exists fails"""
        payload = {
            'user': self.user,
            'name': 'Finx',
            'description': 'This is the best pain killer',
            'med_form': Medicine.MedicineForm.GLOBULES,
            'med_type': Medicine.MedicineType.VITAMIN,
        }
        # create_medicine(**payload)
        Medicine.objects.create(user=self.user,
                                name='Finx',
                                description='This is the best pain killer',
                                med_form=Medicine.MedicineForm.GLOBULES,
                                med_type=Medicine.MedicineType.VITAMIN,)
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_medicine_invalid_med_form_fail(self):
        """"Test creating medicine with broken payload(med_form) must fail"""
        payload = {
            'user': self.user,
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
            'user': self.user,
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': Medicine.MedicineForm.GLOBULES,
            'med_type': 'Something',
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
