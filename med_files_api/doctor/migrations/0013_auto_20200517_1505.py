# Generated by Django 3.0.5 on 2020-05-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0012_auto_20200511_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('URO', 'Urologist'), ('ORT', 'Orthopedist'),
                                            ('OPH', 'Ophthalmologist'), ('NEU', 'Neurologist'),
                                            ('SUR', 'Surgeon'), ('LAR', 'Laryngologist'),
                                            ('GYN', 'Gynecologist'), ('FDO', 'Family doctor'),
                                            ('CAR', 'Cardiologist'), ('ONC', 'Oncologist'),
                                            ('GAS', 'Gastroenterologist'), ('END', 'Endocrinologist'),
                                            ('DER', 'Dermatologist'), ('ALL', 'Allergist')],
                                   default='FDO', max_length=3, verbose_name='Specialization'),
        ),
    ]
