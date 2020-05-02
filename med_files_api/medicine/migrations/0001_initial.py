# Generated by Django 3.0.5 on 2020-05-02 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('form', models.CharField(choices=[('TAB', 'Tablets'), ('SYR', 'Surup'), ('DRO', 'Drops'), ('OIN', 'Ointment'), ('GLO', 'Globules')], default='TAB', max_length=3, verbose_name='Form')),
                ('_type', models.CharField(choices=[('ANT', 'Antybiotic'), ('PRO', 'Probiotic'), ('VIT', 'Vitamin'), ('SUP', 'Suplement')], default='VIT', max_length=3, verbose_name='Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
