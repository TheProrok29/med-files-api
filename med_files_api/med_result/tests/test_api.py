from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
import tempfile
from PIL import Image
from ..models import MedResult, MedImage
from ..serializers import MedImageSerializer


MED_IMAGE_URL = reverse('api:med_image-list')
MED_RESULT_URL = reverse('api:med_result-list')


def sample_med_result(user, **params):
    """Create and return a sample med result"""
    defaults = {
        'name': 'Lorem ipsum',
    }
    defaults.update(params)
    return MedResult.objects.create(user=user, **defaults)


def image_upload_url():
    """Return URL for med result image upload"""
    return reverse('api:med_image-list')


class PublicMedImageApiTest(APITestCase):
    """Test the public med_image API endpoint"""

    def test_login_required(self):
        """Test that login is required to retrieve med_image API endpoint"""
        res = self.client.get(MED_IMAGE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateMedImageApiTest(APITestCase):
    """Test the private med_image API endpoints"""

    def setUp(self):
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)
        self.med_result = sample_med_result(user=self.user)

    def tearDown(self):
        med_images = MedImage.objects.all()
        [m.image.delete() for m in med_images]

    def test_retrieve_med_images(self):
        """Test retrieving med_images"""
        MedImage.objects.create(user=self.user, name='First')
        MedImage.objects.create(user=self.user, name='Second')
        res = self.client.get(MED_IMAGE_URL)
        med_images = MedImage.objects.all().order_by('-name')
        serializer = MedImageSerializer(med_images, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_upload_image_to_med_image(self):
        """Test uploading image to med image"""
        url = image_upload_url()
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10, 10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(url, {'name': 'Morfology 1', 'image': ntf,
                                         'med_result': self.med_result.id}, format='multipart')
        # self.med_result.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn('image', res.data)
        # self.assertTrue(os.path.exists(self.med_result.image.path))

    def test_upload_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url()
        res = self.client.post(url, {'name': 'Morfology 1', 'image': 'xxx',
                                     'med_result': self.med_result.id}, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
