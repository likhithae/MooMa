# Generated by Django 3.0.5 on 2020-05-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200517_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerprofile',
            name='Mooma_user_id',
            field=models.BigIntegerField(default=0),
        ),
    ]