# Generated by Django 3.0.5 on 2020-05-18 09:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200517_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerprofile',
            name='Installed_date',
            field=models.DateField(blank=True, default=datetime.date(2020, 5, 18)),
        ),
    ]
