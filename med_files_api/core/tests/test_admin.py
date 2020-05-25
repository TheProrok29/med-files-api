from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from doctor.models import Doctor
from med_result.models import MedResult, MedImage
from medicine.models import Medicine
from rest_framework import status
from visit.models import Visit

from ..models import Tag


class AdminSiteUserTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='ida@gmail.com',
            password='password1234,',
            name='Super Woman'
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_create_page(self):
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_delete_page(self):
        url = reverse('admin:core_user_delete', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminSiteDoctorTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.doctor = Doctor.objects.create(user=self.admin_user,
                                            name='Tom Hardy',
                                            address='Warsaw, Chrobrego 25/4a',
                                            phone_number='765789432',
                                            specialization=Doctor.DoctorSpecialization.GYNECALOGIST)

    def test_doctor_listed(self):
        url = reverse('admin:doctor_doctor_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.doctor.name)
        self.assertContains(res, self.doctor.address)

    def test_doctor_change_page(self):
        url = reverse('admin:doctor_doctor_change', args=[self.doctor.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_doctor_create_page(self):
        url = reverse('admin:doctor_doctor_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_doctor_delete_page(self):
        url = reverse('admin:doctor_doctor_delete', args=[self.doctor.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminSiteMedicineTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.medicine = Medicine.objects.create(user=self.admin_user,
                                                name='Gripex',
                                                description='This is the best pain killer',
                                                med_form=Medicine.MedicineForm.TABLETS,
                                                med_type=Medicine.MedicineType.PROBIOTIC,)

    def test_medicine_listed(self):
        url = reverse('admin:medicine_medicine_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.medicine.name)
        self.assertContains(res, 'Tablets')
        self.assertContains(res, 'Probiotic')

    def test_medicine_change_page(self):
        url = reverse('admin:medicine_medicine_change', args=[self.medicine.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_medicine_create_page(self):
        url = reverse('admin:medicine_medicine_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_medicine_delete_page(self):
        url = reverse('admin:medicine_medicine_change', args=[self.medicine.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminSiteTagTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.tag = Tag.objects.create(user=self.admin_user, name='Coś')

    def test_tag_listed(self):
        url = reverse('admin:core_tag_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.tag.name)

    def test_tag_change_page(self):
        url = reverse('admin:core_tag_change', args=[self.tag.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_tag_create_page(self):
        url = reverse('admin:core_tag_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_tag_delete_page(self):
        url = reverse('admin:core_tag_delete', args=[self.tag.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminSiteMedResultTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.med_result = MedResult.objects.create(user=self.admin_user, name='Medical result 1')

    def test_med_result_listed(self):
        url = reverse('admin:med_result_medresult_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.med_result.name)

    def test_med_result_change_page(self):
        url = reverse('admin:med_result_medresult_change', args=[self.med_result.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_med_result_create_page(self):
        url = reverse('admin:med_result_medresult_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_med_result_delete_page(self):
        url = reverse('admin:med_result_medresult_delete', args=[self.med_result.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminSiteMedImageTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.med_image = MedImage.objects.create(user=self.admin_user, name='Medical image 1')

    def test_med_image_listed(self):
        url = reverse('admin:med_result_medimage_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.med_image.name)

    def test_med_image_change_page(self):
        url = reverse('admin:med_result_medimage_change', args=[self.med_image.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_med_image_create_page(self):
        url = reverse('admin:med_result_medimage_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_med_image_delete_page(self):
        url = reverse('admin:med_result_medimage_delete', args=[self.med_image.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminSiteVisitTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.visit = Visit.objects.create(user=self.admin_user, name='Visit 1')

    def test_visit_listed(self):
        url = reverse('admin:visit_visit_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.visit.name)

    def test_visit_change_page(self):
        url = reverse('admin:visit_visit_change', args=[self.visit.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_visit_create_page(self):
        url = reverse('admin:visit_visit_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_visit_delete_page(self):
        url = reverse('admin:visit_visit_delete', args=[self.visit.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
