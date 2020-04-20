from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from doctor.models import Doctor
from django.urls import reverse
from rest_framework import status


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

    def test_users_listed(self):
        """Test that users  are listed on admin user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the custom user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_user_create_page(self):
        """Test that the custom user create page works"""
        url = reverse('admin:core_user_add')
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
        self.doctor = Doctor.objects.create(name='Tom Hardy',
                                            adres='Warsaw, Chrobrego 25/4a',
                                            phone_number='765789432',
                                            doc_type=Doctor.DoctorSpecialization.SURGEON,)

    def test_doctors_listed(self):
        """Test that doctors are listed on doctor admin page"""
        url = reverse('admin:doctor_doctor_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.doctor.name)
        self.assertContains(res, self.doctor.adres)

    def test_doctor_change_page(self):
        """Test that the doctor edit page works"""
        url = reverse('admin:doctor_doctor_change', args=[self.doctor.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_doctor_create_page(self):
        """Test that the doctor create page works"""
        url = reverse('admin:doctor_doctor_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
