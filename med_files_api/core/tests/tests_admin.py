from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from doctor.models import Doctor, DoctorSpecialization
from medicine.models import Medicine
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

    def test_user_delete_page(self):
        """Test that the custom user delete page works"""
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
        self.spec = DoctorSpecialization.objects.create(name='Surgeon')
        self.doctor = Doctor.objects.create(user=self.admin_user,
                                            name='Tom Hardy',
                                            adres='Warsaw, Chrobrego 25/4a',
                                            phone_number='765789432',
                                            specialization=self.spec)

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

    def test_doctor_delete_page(self):
        """Test that the doctor delete page works"""
        url = reverse('admin:doctor_doctor_delete', args=[self.doctor.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminSiteDoctorSpecializationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='tom@gmail.com',
            password='password1234$$ ,'
        )
        self.client.force_login(self.admin_user)
        self.spec = DoctorSpecialization.objects.create(name='Surgeon')

    def test_doctors_specialization_listed(self):
        """Test that doctors specialziation are listed on doctor specialization admin page"""
        url = reverse('admin:doctor_doctorspecialization_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.spec.name)

    def test_doctor_specialziation_change_page(self):
        """Test that the doctor specialization edit page works"""
        url = reverse('admin:doctor_doctorspecialization_change', args=[self.spec.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_doctor_specialziation_create_page(self):
        """Test that the doctor specialziation create page works"""
        url = reverse('admin:doctor_doctorspecialization_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_doctor_specialziation_delete_page(self):
        """Test that the doctor specialization delete page works"""
        url = reverse('admin:doctor_doctorspecialization_change', args=[self.spec.id])
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
        self.medicine = Medicine.objects.create(name='Gripex',
                                                description='This is the best pain killer',
                                                med_form=Medicine.MedicineForm.TABLETS,
                                                med_type=Medicine.MedicineType.PROBIOTIC,)

    def test_medicines_listed(self):
        """Test that dmedicines are listed on medicine admin page"""
        url = reverse('admin:medicine_medicine_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertContains(res, self.medicine.name)
        self.assertContains(res, 'Tablets')
        self.assertContains(res, 'Probiotic')

    def test_medicine_change_page(self):
        """Test that the medicine edit page works"""
        url = reverse('admin:medicine_medicine_change', args=[self.medicine.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_medicine_create_page(self):
        """Test that the medicine create page works"""
        url = reverse('admin:medicine_medicine_add')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_medicine_delete_page(self):
        """Test that the medicine delete page works"""
        url = reverse('admin:medicine_medicine_change', args=[self.medicine.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
