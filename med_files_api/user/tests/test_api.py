import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

CREATE_USER_URL = reverse('api:user-list')
TOKEN_URL = reverse('user:token')
ME_URL = reverse('user:me')
ME_AUTH_URL = reverse('user:auth')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(APITestCase):
    """
    Test the users API (public).
    """

    def test_create_valid_user_success(self):
        payload = {
            'email': 'test@vp.pl',
            'password': 'somepassword',
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        payload = {
            'email': 'test@vp.pl',
            'password': 'somepassword'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_to_short(self):
        """
        Test that the password must be more than 5 characters.
        """
        payload = {'email': 'tom@vp.pl', 'password': 'abc'}
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        payload = {'email': 'aaass@vp.pl', 'password': 'testpass'}
        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        create_user(email='abc@gmail.com', password='testpass')
        payload = {'email': 'abc@gmail.com', 'password': 'notestpass'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user_fail(self):
        payload = {'email': 'abc@gmail.com', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_password_field_fail(self):
        payload = {'email': 'abc@gmail.com', 'password': ''}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_email_field_fail(self):
        payload = {'email': '', 'password': 'testpass'}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized_fail(self):
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(APITestCase):
    """
    Test API requests that require authentication.
    """

    def setUp(self):
        self.user = create_user(
            email='prorok292vp.pl',
            password='testpass',
            name='Tom Fakir',
            born_date='1992-11-29'
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_data_success(self):
        res = self.client.get(ME_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'id': self.user.id,
            'name': self.user.name,
            'born_date': self.user.born_date,
        })

    def test_retrieve_profile_authentication_data_success(self):
        res = self.client.get(ME_AUTH_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'id': self.user.id,
            'email': self.user.email,
        })
        self.assertTrue(self.user.check_password('testpass'))

    def test_post_not_allowed(self):
        res = self.client.post(ME_URL, {})
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_auth_data(self):
        payload = {'email': 'advvfaf@vp.pl', 'password': 'newpassword123'}
        res = self.client.patch(ME_AUTH_URL, payload)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, payload['email'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_update_user_data(self):
        payload = {'name': 'Jan Kowalski', 'born_date': datetime.date(1989, 7, 11)}
        res = self.client.patch(ME_URL, payload)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertEqual(self.user.born_date, payload['born_date'])
        self.assertEqual(res.status_code, status.HTTP_200_OK)
