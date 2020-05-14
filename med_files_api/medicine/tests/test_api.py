from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from ..models import Medicine
from ..serializers import MedicineSerializer


MEDICINE_URL = reverse('api:medicine-list')


def get_medicine_detail_url(medicine):
    """Return detail url for medicine instance passed as a parametr"""
    return reverse('api:medicine-detail', kwargs={'pk': medicine.pk})


class PublicMedicineApiTest(APITestCase):
    """Test the public medicine API endpoint"""

    def test_login_required(self):
        """Test that login is required to retrieve medicine API endpoint"""
        res = self.client.get(MEDICINE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMedicineApiTest(APITestCase):
    """Test the private medicine API endpoints"""

    def setUp(self):
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)
        self.new_medicine = Medicine.objects.create(user=self.user, name='Postin')

    def test_retrieve_medicines(self):
        """Test retrieving medicines"""
        Medicine.objects.create(user=self.user, name='Alkamenkun')
        Medicine.objects.create(user=self.user, name='Dioxin')
        res = self.client.get(MEDICINE_URL)
        medicines = Medicine.objects.all().order_by('-name')
        serializer = MedicineSerializer(medicines, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_medicine_with_full_data_success(self):
        """Test createing medicine with valid payload is successful"""
        payload = {
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
            'name': 'Apap',
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        medicine = Medicine.objects.get(**res.data)
        self.assertTrue(medicine.name, payload['name'])

    def test_medicine_exists(self):
        """Test creating medicine that already exists fails"""
        payload = {
            'name': 'Finx',
        }
        Medicine.objects.create(user=self.user,
                                name='Finx')
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_medicine_invalid_med_form_fail(self):
        """"Test creating medicine with broken payload(med_form) must fail"""
        payload = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_form': 'Something',
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_medicine_invalid_med_type_fail(self):
        """Test creating medicine with broken payload(med_type) must fail"""
        payload = {
            'name': 'New one',
            'description': 'This is the best pain killer',
            'med_type': 'Something',
        }
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_see_only_user_medicines(self):
        """Show only medicines who were created by the logged in user"""
        Medicine.objects.create(user=self.user, name='Makumba')
        new_user = get_user_model().objects.create_user('frankbbf@gmail.pl', 'testpasswd')
        Medicine.objects.create(user=new_user, name='Parumba')
        self.client.force_authenticate(new_user)
        res = self.client.get(MEDICINE_URL)
        self.assertNotContains(res, 'Makumba')
        self.assertContains(res, 'Parumba')

    def test_delete_medicine(self):
        """Test deleting existing medicine"""
        res = self.client.delete(get_medicine_detail_url(self.new_medicine))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_medicine(self):
        """Test updating existing medicine"""
        payload = {
            'description': 'Best antybiotic',
            'med_type': Medicine.MedicineType.ANTIBIOTIC,
            'med_form': Medicine.MedicineForm.SYRUP
        }
        res = self.client.patch(get_medicine_detail_url(self.new_medicine), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.new_medicine.refresh_from_db()
        self.assertEqual(self.new_medicine.description, payload['description'])
        self.assertEqual(self.new_medicine.med_form, payload['med_form'])

    def test_create_the_same_medicine_for_different_user_success(self):
        """Test creating the same medicine for different user must be success"""
        Medicine.objects.create(user=self.user, name='Makumba')
        new_user = get_user_model().objects.create_user('kalika@gmail.com', 'tesrfgtpasswd')
        payload = {
            'user': new_user,
            'name': 'Makumba'
        }
        self.client.force_authenticate(new_user)
        res = self.client.post(MEDICINE_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
