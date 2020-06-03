# Generated by Django 3.0.5 on 2020-05-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='financierprofile',
            name='bank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.bank'),
        ),
        migrations.AddField(
            model_name='financierprofile',
            name='branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.branch'),
        ),
        migrations.AddField(
            model_name='financierprofile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.ACity'),
        ),
        migrations.AddField(
            model_name='financierprofile',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.District'),
        ),
        migrations.AddField(
            model_name='financierprofile',
            name='ifsccode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.ifsc'),
        ),
    ]
