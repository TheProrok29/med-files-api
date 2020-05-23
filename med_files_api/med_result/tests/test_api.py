import tempfile

from PIL import Image
from core.models import Tag
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from visit.models import Visit
from doctor.models import Doctor
from ..models import MedResult, MedImage
from ..serializers import MedImageSerializer, MedResultSerializer, MedResultDetailSerializer

MED_IMAGE_URL = reverse('api:med_image-list')
MED_RESULT_URL = reverse('api:med_result-list')


def sample_med_result(user, **params):
    """
    Create and return a sample med result.
    """
    defaults = {
        'name': 'Lorem ipsum',
    }
    defaults.update(params)
    return MedResult.objects.create(user=user, **defaults)


def get_med_image_detail_url(med_image):
    """
    Return detail url for med image instance passed as a parametr.
    """
    return reverse('api:med_image-detail', kwargs={'pk': med_image.pk})


def get_med_result_detail_url(med_result):
    """
    Return detail url for med result instance passed as a parametr.
    """
    return reverse('api:med_result-detail', kwargs={'pk': med_result.pk})


class PublicMedImageApiTest(APITestCase):
    """
    Test the public med image API.
    """

    def test_login_required(self):
        res = self.client.get(MED_IMAGE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMedImageApiTest(APITestCase):
    """
    Test the private med image API.
    """

    def setUp(self):
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)
        self.med_result = sample_med_result(user=self.user)
        self.med_image = MedImage.objects.create(user=self.user, name='Image 1')

    def tearDown(self):
        med_images = MedImage.objects.all()
        [m.image.delete() for m in med_images]

    def test_retrieve_med_images(self):
        MedImage.objects.create(user=self.user, name='First')
        MedImage.objects.create(user=self.user, name='Second')
        res = self.client.get(MED_IMAGE_URL)
        med_images = MedImage.objects.all().order_by('-name')
        serializer = MedImageSerializer(med_images, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_med_image_with_full_data_success(self):
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10, 10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(MED_IMAGE_URL, {'name': 'Morfology 1', 'image': ntf,
                                                   'med_result': self.med_result.id}, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('image', res.data)

    def test_create_med_image_without_image_success(self):
        res = self.client.post(MED_IMAGE_URL, {'name': 'Morfology 1',
                                               'med_result': self.med_result.id}, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_upload_image_bad_request_fail(self):
        res = self.client.post(MED_IMAGE_URL, {'name': 'Morfology 1', 'image': 'xxx',
                                               'med_result': self.med_result.id}, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_med_image_limited_to_user(self):
        MedImage.objects.create(user=self.user, name='Photo 1')
        new_user = get_user_model().objects.create_user('frankbbf@gmail.pl', 'testpasswd')
        MedImage.objects.create(user=new_user, name='Photo 2')
        self.client.force_authenticate(new_user)
        res = self.client.get(MED_IMAGE_URL)
        self.assertNotContains(res, 'Photo 1')
        self.assertContains(res, 'Photo 2')

    def test_delete_med_image(self):
        res = self.client.delete(get_med_image_detail_url(self.med_image))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_med_image(self):
        payload = {
            'name': 'Rentgen',
            'med_result': self.med_result.id
        }
        res = self.client.patch(get_med_image_detail_url(self.med_image), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.med_image.refresh_from_db()
        self.assertEqual(self.med_image.name, payload['name'])


class PublicMedResultApiTest(APITestCase):
    """
    Test the public med result API.
    """

    def test_login_required(self):
        """Test that login is required to retrieve med_result API endpoint"""
        res = self.client.get(MED_RESULT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMedResultApiTest(APITestCase):
    """
    Test the private med result API.
    """

    def setUp(self):
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)
        self.med_result = sample_med_result(user=self.user)
        self.med_image = MedImage.objects.create(user=self.user, name='Image 1')
        self.tag = Tag.objects.create(user=self.user, name='Head')
        self.visit = Visit.objects.create(user=self.user,
                                          name='Wizyta Urologiczna',
                                          doctor=Doctor.objects.create(user=self.user, name='Jan Kowalski'))

    def test_retrieve_med_result(self):
        med1 = MedResult.objects.create(user=self.user, name='First',
                                        description='ABCD',
                                        date_of_exam=timezone.now().date(),
                                        visit=self.visit)
        med1.tag.add(self.tag)
        med2 = MedResult.objects.create(user=self.user, name='Second',
                                        description='DCBA',
                                        date_of_exam=timezone.now().date(),
                                        visit=self.visit)
        med2.tag.add(self.tag)
        res = self.client.get(MED_RESULT_URL)
        med_results = MedResult.objects.all().order_by('-name')
        serializer = MedResultSerializer(med_results, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_med_result_with_full_data_success(self):
        payload = {
            'name': 'Badanie laryngologiczne',
            'description': 'Badanie nosa po operacji przegrody',
            'date_of_exam': timezone.now().date(),
            'visit': self.visit.id,
            'tag': self.tag.id,
        }
        res = self.client.post(MED_RESULT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_med_result_with_min_data_success(self):
        payload = {
            'name': 'Badanie laryngologiczne',
        }
        res = self.client.post(MED_RESULT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_med_result_invalid_tag_fail(self):
        payload = {
            'name': 'New one',
            'tag': 'Something',
        }
        res = self.client.post(MED_RESULT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_med_result_invalid_visit_fail(self):
        payload = {
            'name': 'New one',
            'visit': 'Something',
        }
        res = self.client.post(MED_RESULT_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_med_result_limited_to_user(self):
        MedResult.objects.create(user=self.user, name='Result 1')
        new_user = get_user_model().objects.create_user('frankbbf@gmail.pl', 'testpasswd')
        MedResult.objects.create(user=new_user, name='Result 2')
        self.client.force_authenticate(new_user)
        res = self.client.get(MED_RESULT_URL)
        self.assertNotContains(res, 'Result 1')
        self.assertContains(res, 'Result 2')

    def test_delete_med_result(self):
        res = self.client.delete(get_med_result_detail_url(self.med_result))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_med_result(self):
        payload = {
            'name': 'Badanie gastrologiczne',
        }
        res = self.client.patch(get_med_result_detail_url(self.med_result), payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.med_result.refresh_from_db()
        self.assertEqual(self.med_result.name, payload['name'])

    def test_view_med_result_detail(self):
        med_result = sample_med_result(user=self.user)
        med_result.tag.add(self.tag)
        url = get_med_result_detail_url(med_result)
        res = self.client.get(url)
        serializer = MedResultDetailSerializer(med_result)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
