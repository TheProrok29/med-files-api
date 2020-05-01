from django.urls import reverse
from ..models import DoctorSpecialization
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from ..serializers import DoctorSpecializationSerializer


DOC_SPECIALIZATION_URL = reverse('api:doctor_specialization-list')


class PublicDoctorSpecializationApiTests(APITestCase):
    """Test the publicly available Doctor Specialization API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving Doctor API endpoint"""
        res = self.client.get(DOC_SPECIALIZATION_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateDoctorSpecializationApiTest(APITestCase):
    """Test the autorized Doctor Specialization API"""

    def setUp(self):
        self.client = APIClient()
        self.user1 = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.user2 = get_user_model().objects.create_user('adam@gmail.com.pl', 'testpasswd2')
        self.client.force_authenticate(self.user1)

    def test_doctor_specialization_endpoint_available(self):
        """Test  doctor specialization endpoint is available"""
        response = self.client.get(DOC_SPECIALIZATION_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_doc_specialization(self):
        """Test retrieving doctor specializations"""
        DoctorSpecialization.objects.create(name='Surgeon')
        DoctorSpecialization.objects.create(name='Ginecologist')
        res = self.client.get(DOC_SPECIALIZATION_URL)
        doc_specs = DoctorSpecialization.objects.all().order_by('-name')
        serializer = DoctorSpecializationSerializer(doc_specs, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_doctor_specialization_success(self):
        """Test createing doctor specialization is successful"""
        payload = {'name': 'Laryngologist', }
        res = self.client.post(DOC_SPECIALIZATION_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        doc_spec = DoctorSpecialization.objects.get(**res.data)
        self.assertTrue(doc_spec.name, payload['name'])

    def test_doctor_specialization_exists(self):
        """Test creating doctor specialization that already exists fails"""
        DoctorSpecialization.objects.create(name='Laryngologist')
        payload = {'name': 'Laryngologist', }
        res = self.client.post(DOC_SPECIALIZATION_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_doctor_specialization(self):
        """Test deleting doctor specialization"""
        new_doc_spec = DoctorSpecialization.objects.create(name='Laryngologist')
        DEL_SPEC_URL = reverse('api:doctor_specialization-detail', kwargs={'pk': new_doc_spec.pk})
        res = self.client.delete(DEL_SPEC_URL)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_doctor_specialization(self):
        """Test update existing doctor specialziation"""
        new_doc_spec = DoctorSpecialization.objects.create(name='Sawbones')
        DEL_SPEC_URL = reverse('api:doctor_specialization-detail', kwargs={'pk': new_doc_spec.pk})
        payload = {'name': 'Surgeon'}
        res = self.client.patch(DEL_SPEC_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
