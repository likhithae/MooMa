# Generated by Django 3.0.5 on 2020-05-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200517_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmerprofile',
            name='Others',
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='Mixed_breed',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='Other_breed',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
