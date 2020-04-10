# Generated by Django 3.0.5 on 2020-04-10 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('adres', models.CharField(max_length=200, verbose_name='Adres')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True, unique=True, verbose_name='Phone Number')),
                ('doc_type', models.CharField(choices=[('URO', 'Urologis'), ('ORT', 'Orthopedist'), ('OPH', 'Ophthalmologist'), ('NEU', 'Neurologist'), ('SUR', 'Surgeon'), ('LAR', 'Laryngologist'), ('GYN', 'Gynecologist'), ('FDO', 'Family doctor'), ('CAR', 'Cardiologist'), ('ONC', 'Oncologist'), ('GAS', 'Gastroenterologist'), ('END', 'Endocrinologist.'), ('DER', 'Dermatologist'), ('ALL', 'Allergist')], default='FDO', max_length=3, verbose_name='Specialization')),
            ],
        ),
    ]
