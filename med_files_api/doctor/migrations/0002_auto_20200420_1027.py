# Generated by Django 3.0.5 on 2020-04-20 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='adres',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Adres'),
        ),
    ]