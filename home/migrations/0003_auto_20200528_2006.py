# Generated by Django 3.0.5 on 2020-05-28 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200527_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='Installed_date',
            field=models.DateField(default=datetime.date(2020, 5, 28)),
        ),
    ]