# Generated by Django 3.0.5 on 2020-05-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_result', '0005_auto_20200509_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medresult',
            name='date_of_exam',
            field=models.DateField(blank=True, null=True),
        ),
    ]
