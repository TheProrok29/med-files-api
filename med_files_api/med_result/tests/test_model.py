from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ..models import MedResult, MedImage, med_result_file_path


class MedResultModelTest(TestCase):

    def test_create_med_result(self):
        """Test creating a new med result"""
        med_result = MedResult.objects.create(
            user=get_user_model().objects.create_user(email='prorowk29@vp.pl', password='pa$$w0rd'),
            name='Lorem Ipsum',
            date_of_exam=timezone.now())
        self.assertTrue(isinstance(med_result, MedResult))
        self.assertEqual(med_result.__str__(), med_result.name)

    def test_med_result_str(self):
        """Test medical result string representation"""
        med_result = MedResult.objects.create(
            user=get_user_model().objects.create_user(email='prorowk29@vp.pl', password='pa$$w0rd'),
            name='Lorem Ipsum',
            date_of_exam=timezone.now())
        self.assertEqual(str(med_result), med_result.name)


class MedResultImageModelTest(TestCase):
    def test_med_result_str(self):
        """Test medical result image string representation"""
        med_image = MedImage.objects.create(
            user=get_user_model().objects.create_user(email='prorowk29@vp.pl', password='pa$$w0rd'),
            name='Lorem Ipsum')
        self.assertEqual(str(med_image), med_image.name)

    @patch('uuid.uuid4')
    def test_result_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = med_result_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/med_result/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
