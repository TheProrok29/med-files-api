# Generated by Django 3.0.5 on 2020-05-09 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='visit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
