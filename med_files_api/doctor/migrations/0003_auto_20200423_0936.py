# Generated by Django 3.0.5 on 2020-04-23 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20200420_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='doc_type',
            new_name='doc_spec',
        ),
    ]
