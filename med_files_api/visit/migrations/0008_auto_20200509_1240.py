# Generated by Django 3.0.5 on 2020-05-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0007_auto_20200509_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
