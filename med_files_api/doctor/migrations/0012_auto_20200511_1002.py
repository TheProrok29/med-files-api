# Generated by Django 3.0.5 on 2020-05-11 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_auto_20200504_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='adres',
            new_name='address',
        ),
    ]
