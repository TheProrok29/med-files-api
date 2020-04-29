from django.urls import reverse
from ..models import Doctor, DoctorSpecialization
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ..serializers import DoctorSerializer
DOCTOR_URL = reverse('api:doctor-list')


class PublicDoctorApiTests(APITestCase):
    """Test the publicly available Doctor API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving Doctor API endpoint"""
        res = self.client.get(DOCTOR_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateDoctorApiTest(APITestCase):
    """Test the autorized Doctor API"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)
        self.spec = DoctorSpecialization.objects.create(name='Laryngologist')

    def test_doctor_endpoint_available(self):
        """Test  doctor endpoint is available"""
        response = self.client.get(DOCTOR_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_doctors(self):
        """Test retrieving doctors"""
        Doctor.objects.create(
            user=self.user,
            name='Fakren Makrewn',
            specialization=self.spec,
        )
        Doctor.objects.create(
            user=self.user,
            name='Ankins Heliosferos',
            specialization=self.spec,
        )
        res = self.client.get(DOCTOR_URL)
        doctors = Doctor.objects.all().order_by('-name')
        serializer = DoctorSerializer(doctors, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_doctor_with_full_data_success(self):
        """Test createing doctor with valid payload is successful"""
        payload = {
            'name': 'Fakren Makrewn',
            'adres': 'Opole 24/b',
            'phone_number': '456789086',
            'specialization': self.spec.id,
        }
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        doctor = Doctor.objects.get(**res.data)
        self.assertTrue(doctor.name, payload['name'])

    def test_create_doctor_with_min_data_success(self):
        """Test createing doctor with valid min payload is successful"""
        payload = {
            'name': 'Fakren Makrewn',
            'specialization': self.spec.id,
        }
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        doctor = Doctor.objects.get(**res.data)
        self.assertTrue(doctor.name, payload['name'])

    def test_doctor_exists(self):
        """Test creating doctor that already exists fails"""
        payload = {
            'user': self.user,
            'name': 'Fakren Makrewn',
            'adres': 'Opole 24/b',
            'phone_number': '456789086',
            'specialization': self.spec.id,
        }
        Doctor.objects.create(
            user=self.user,
            name='Fakren Makrewn',
            adres='Opole 24/b',
            phone_number='456789086',
            specialization=self.spec)
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_doctor_invalid_specialization_fail(self):
        """"Test creating doctor with broken payload(specialziation) must fail"""
        payload = {
            'name': 'Fakren Makrewn',
            'adres': 'Opole 24/b',
            'phone_number': '456789086',
            'specialization': 'Something',
        }
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
