# Generated by Django 3.0.5 on 2020-05-23 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_auto_20200517_1505'),
        ('visit', '0012_remove_visit_med_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True,
                                    on_delete=django.db.models.deletion.SET_NULL, to='doctor.Doctor'),
        ),
    ]
