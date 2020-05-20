# Generated by Django 3.0.5 on 2020-05-18 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med_result', '0009_auto_20200517_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medimage',
            name='med_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='images', to='med_result.MedResult'),
        ),
    ]