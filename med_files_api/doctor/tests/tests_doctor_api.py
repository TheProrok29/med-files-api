from django.urls import reverse
from ..models import Doctor, DoctorSpecialization
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
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
        self.new_doctor = Doctor.objects.create(
            user=self.user,
            name='Oleg Faustin',
            adres='Warsaw 25/b',
            phone_number='478789086',
            specialization=self.spec)
        self.DOCTOR_DETAIL_URL = reverse('api:doctor-detail', kwargs={'pk': self.new_doctor.pk})

    def test_doctor_endpoint_available(self):
        """Test  doctor endpoint is available"""
        res = self.client.get(DOCTOR_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

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
            'name': 'Oleg Faustin',
            'adres': 'Opole 24/b',
            'phone_number': '456789086',
            'specialization': self.spec.id,
        }
        res = self.client.post(DOCTOR_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show_only_user_doctor(self):
        """Show only doctors who were created by the logged in user"""
        Doctor.objects.create(
            user=self.user,
            name='Mikael Blumberg',
            specialization=self.spec)
        new_user = get_user_model().objects.create_user('frankbbf@gmail.pl', 'testpasswd')
        Doctor.objects.create(
            user=new_user,
            name='Pat Sement',
            specialization=self.spec)
        self.client.force_authenticate(new_user)
        res = self.client.get(DOCTOR_URL)
        self.assertNotContains(res, 'Mikael Blumberg')
        self.assertContains(res, 'Pat Sement')

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

    def test_delete_doctor(self):
        """Test deleting doctor"""
        res = self.client.delete(self.DOCTOR_DETAIL_URL)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_doctor(self):
        """Test update existing doctor"""
        payload = {
            'name': 'Fakren Makrewn',
            'adres': 'Warsaw 24/b',
            'phone_number': '987654321',
            'specialization': self.spec.id,
        }
        res = self.client.patch(self.DOCTOR_DETAIL_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
