from core.models import Tag
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from doctor.models import Doctor
from med_result.models import MedResult
from medicine.models import Medicine
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Visit
from ..serializers import VisitSerializer, VisitDetailSerializer

VISIT_URL = reverse('api:visit-list')


def get_visit_detail_url(visit):
    """
    Return detail url for visit instance passed as a parametr.
    """
    return reverse('api:visit-detail', kwargs={'pk': visit.pk})


class PublicVisitApiTest(APITestCase):
    """
    Test the public visit API.
    """

    def test_login_required(self):
        res = self.client.get(VISIT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateVisitApiTest(APITestCase):
    """
    Test the private visit API.
    """

    def setUp(self):
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)
        self.doctor = Doctor.objects.create(user=self.user, name='Jan Kowalski')
        self.medicine = Medicine.objects.create(user=self.user, name='Apap')
        self.tag = Tag.objects.create(user=self.user, name='Wro')
        self.med_result = MedResult.objects.create(user=self.user, name='Head Rentgen', date_of_exam=timezone.now())
        self.new_visit = Visit.objects.create(user=self.user, name='Wizyta Jakaśtam')

    def test_retrieve_visit(self):
        visit1 = Visit.objects.create(user=self.user,
                                      visit_date=timezone.now().date(),
                                      name='Wizyta Laryngologiczna',
                                      address='Opole Chrobrego 24/3d',
                                      doctor=self.doctor)
        visit1.medicine.add(self.medicine)
        visit1.tag.add(self.tag)
        visit2 = Visit.objects.create(user=self.user,
                                      visit_date=timezone.now().date(),
                                      name='Wizyta Jakaśtam',
                                      address='Wrocław Armii Krajowej 1d/2',
                                      doctor=self.doctor)
        visit2.medicine.add(self.medicine)
        visit2.tag.add(self.tag)
        res = self.client.get(VISIT_URL)
        visits = Visit.objects.all().order_by('-name')
        serializer = VisitSerializer(visits, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_visit_with_full_data_success(self):
        payload = {
            'name': 'Wizyta Laryngologiczna',
            'address': 'Wrocław Armii Krajowej 1d/2',
            'doctor': self.doctor.id,
            'medicine': self.medicine.id,
            'visit_date': timezone.now().date(),
            'tag': self.tag.id,
        }
        res = self.client.post(VISIT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_visit_with_min_data_success(self):
        payload = {'name': 'Wizyta Laryngologiczna', }
        res = self.client.post(VISIT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_visit_without_name_fail(self):
        payload = {
            'doctor': self.doctor.id,
        }
        res = self.client.post(VISIT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_visit_limited_to_user(self):
        Visit.objects.create(user=self.user, name='Wizyta 1')
        new_user = get_user_model().objects.create_user('frankbbf@gmail.pl', 'testpasswd')
        Visit.objects.create(user=new_user, name='Wizyta 2')
        self.client.force_authenticate(new_user)
        res = self.client.get(VISIT_URL)
        self.assertNotContains(res, 'Wizyta 1')
        self.assertContains(res, 'Wizyta 2')

    def test_delete_visit(self):
        res = self.client.delete(get_visit_detail_url(self.new_visit))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_visit(self):
        payload = {
            'address': 'Obórki 63b',
        }
        res = self.client.patch(get_visit_detail_url(self.new_visit), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.new_visit.refresh_from_db()
        self.assertEqual(self.new_visit.address, payload['address'])

    def test_view_visit_detail(self):
        visit = Visit.objects.create(user=self.user,
                                     visit_date=timezone.now().date(),
                                     name='Wizyta Laryngologiczna',
                                     address='Opole Chrobrego 24/3d',
                                     doctor=self.doctor)
        visit.tag.add(self.tag)
        visit.medicine.add(self.medicine)
        visit.med_result.add(self.med_result)
        url = get_visit_detail_url(visit)
        res = self.client.get(url)
        serializer = VisitDetailSerializer(visit)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
