from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

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
        """Test that users  are listed on user page"""
        url = reverse('admin:users_user_changelist')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the custom user edit page works"""
        url = reverse('admin:users_user_change', args=[self.user.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)