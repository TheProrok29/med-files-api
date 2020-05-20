from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Tag


class UserModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@something.com'
        password = 'Testpassword123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new iuser is normalized"""
        email = 'test@vdFDGp.pl'
        user = get_user_model().objects.create_user(email, 'pass123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test createing usert with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'tom@vp.pl',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


class TagModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@something.com',
            password='Testpassword123'
        )

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = Tag.objects.create(user=self.user, name='Heart')
        self.assertEqual(str(tag), tag.name)
