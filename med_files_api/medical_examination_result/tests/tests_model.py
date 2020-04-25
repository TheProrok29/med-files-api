from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from ..models import MedicalExaminationResult, exam_result_file_path


class MedicalExaminationResultModelTest(TestCase):

    def test_create_exam_result(self):
        """Test creating a new exam  result"""
        med_exam_result = MedicalExaminationResult.objects.create(
            user=get_user_model().objects.create_user(email='prorowk29@vp.pl', password='pa$$w0rd'),
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum',
            date_of_exam=timezone.now())
        self.assertTrue(isinstance(med_exam_result, MedicalExaminationResult))
        self.assertEqual(med_exam_result.__str__(), med_exam_result.description[:100])

    def test_med_exam_result_str(self):
        """Test medical examination result string representation"""
        med_exam_result = MedicalExaminationResult.objects.create(
            user=get_user_model().objects.create_user(email='prorowk29@vp.pl', password='pa$$w0rd'),
            description='Lorem Ipsum is simply dummy text of thddecc printing and typesetting industry. Lorem Ipsum',
            date_of_exam=timezone.now())
        self.assertEqual(str(med_exam_result), med_exam_result.description)

    @patch('uuid.uuid4')
    def test_exam_result_file_name_uuid(self, mock_uuid):
        """Test that image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = exam_result_file_path(None, 'myimage.jpg')

        exp_path = f'uploads/examination_result/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
