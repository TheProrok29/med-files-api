# Generated by Django 3.0.5 on 2020-04-25 16:16

from django.db import migrations, models
import medical_examination_result.models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_examination_result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalexaminationresult',
            name='image',
            field=models.ImageField(null=True, upload_to=medical_examination_result.models.exam_result_file_path),
        ),
    ]
