from unittest.mock import patch

from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from visit.models import Visit
from core.models import Tag
from doctor.models import Doctor
from ..models import MedResult, MedImage, med_image_file_path


class MedResultModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(email='prorowk29@vp.pl', password='pa$$w0rd')
        self.visit = Visit.objects.create(user=self.user,
                                          name='Wizyta Urologiczna',
                                          doctor=Doctor.objects.create(user=self.user, name='Jan Kowalski'))
        self.tag = Tag.objects.create(user=self.user, name='Nofr')

    def test_create_med_result_min_data(self):
        med_result = MedResult.objects.create(
            user=self.user,
            name='Lorem Ipsum')
        self.assertTrue(isinstance(med_result, MedResult))
        self.assertEqual(med_result.__str__(), med_result.name)

    def test_create_med_result_full_data(self):
        med_result = MedResult.objects.create(
            user=self.user,
            name='Lorem Ipsum',
            description='Something went wrong',
            date_of_exam=datetime.now().date(),
            visit=self.visit)
        med_result.tag.add(self.tag)
        self.assertTrue(isinstance(med_result, MedResult))
        self.assertEqual(med_result.tag.count(), 1)
        self.assertEqual(med_result.visit, self.visit)


class MedImageModelTest(TestCase):
    def test_create_med_image(self):
        med_image = MedImage.objects.create(
            user=get_user_model().objects.create_user(email='prorowk29@vp.pl', password='pa$$w0rd'),
            name='Lorem Ipsum')
        self.assertTrue(isinstance(med_image, MedImage))
        self.assertEqual(str(med_image), med_image.name)

    @patch('uuid.uuid4')
    def test_med_image_file_name_uuid(self, mock_uuid):
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = med_image_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/med_result/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
