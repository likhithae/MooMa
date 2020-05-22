# Generated by Django 3.0.5 on 2020-05-19 10:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200518_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.District')),
            ],
        ),
        migrations.RemoveField(
            model_name='farmerprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='farmerprofile',
            name='country',
        ),
        migrations.AlterField(
            model_name='farmerprofile',
            name='Installed_date',
            field=models.DateField(default=datetime.date(2020, 5, 19)),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.State'),
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.District'),
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.State'),
        ),
        migrations.AddField(
            model_name='farmerprofile',
            name='sub_district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.SubDistrict'),
        ),
    ]