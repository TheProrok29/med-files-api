from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Tag
from ..serializers import TagSerializer

TAG_URL = reverse('api:tag-list')


def get_tag_detail_url(tag):
    """Return detail url for tag instance passed as a parametr"""
    return reverse('api:tag-detail', kwargs={'pk': tag.pk})


class PublicTagApiTests(APITestCase):
    """Test the publicly avaialble tags API"""

    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        res = self.client.get(TAG_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagApiTests(APITestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user('prorok@vp.pl', 'testpass')
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        Tag.objects.create(user=self.user, name='Heart')
        Tag.objects.create(user=self.user, name='Head')
        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        res = self.client.get(TAG_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tag_limited_to_user(self):
        """Test that tags returned are for the authenticated user"""
        new_user = get_user_model().objects.create_user('lambado2@gmail.com', 'hardpassevermade')
        Tag.objects.create(user=new_user, name='Leg')
        tag = Tag.objects.create(user=self.user, name='Head')
        res = self.client.get(TAG_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)

    def test_create_tag(self):
        """Test creating a new tag"""
        payload = {'name': 'Test tag'}
        res = self.client.post(TAG_URL, payload)

        exists = Tag.objects.filter(
            user=self.user,
            name=payload['name']
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """Test creating a new tag with invalid payload"""
        payload = {'name': ''}
        res = self.client.post(TAG_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_tag(self):
        """Test updating existing tag"""
        tag = Tag.objects.create(user=self.user, name='Right Leg')
        payload = {'name': 'Left Leg'}
        res1 = self.client.get(get_tag_detail_url(tag))
        res2 = self.client.patch(get_tag_detail_url(tag), payload)
        tag.refresh_from_db()
        self.assertEqual(res1.data['name'], 'Right Leg')
        self.assertEqual(res2.status_code, status.HTTP_200_OK)
        self.assertEqual(res2.data['name'], payload['name'])

    def test_delete_tag(self):
        """Test deleting existing tag"""
        tag = Tag.objects.create(user=self.user, name='Right Leg')
        res = self.client.delete(get_tag_detail_url(tag))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.all().count(), 0)
