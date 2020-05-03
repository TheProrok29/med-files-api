from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
import tempfile
import os
from PIL import Image
from django.utils import timezone
from ..models import MedResult


MED_EXAM_RESULT_URL = reverse('api:med_result-list')


def sample_med_result(user, **params):
    """Create and return a sample med result"""
    defaults = {
        'description': 'sghsgfwshbsfgsfsfgsgs',
        'date_of_exam': timezone.now(),
    }
    defaults.update(params)
    return MedResult.objects.create(user=user, **defaults)


def image_upload_url(med_result_id):
    """Return URL for med result image upload"""
    return reverse('api:med_result-upload-image', args=[med_result_id])


class MedResultImageUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user('prorsok29@vp.pl', 'testpasswd')
        self.client.force_authenticate(self.user)
        self.med_result = sample_med_result(user=self.user)

    def tearDown(self):
        self.med_result.image.delete()

    def test_upload_image_to_med_result(self):
        """Test uploading image to med exam result"""
        url = image_upload_url(self.med_result.id)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10, 10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(url, {'image': ntf}, format='multipart')

        self.med_result.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('image', res.data)
        self.assertTrue(os.path.exists(self.med_result.image.path))

    def test_upload_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url(self.med_result.id)
        res = self.client.post(url, {'image': 'notimage'}, format='multipart')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
