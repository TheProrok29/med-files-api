from django.test import TestCase
from medical_examination_result.models import MedicalExaminationResult
from django.contrib.auth import get_user_model
from django.utils import timezone


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
            description='Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum',
            date_of_exam=timezone.now())
        self.assertEqual(str(med_exam_result), med_exam_result.description)
