# Generated by Django 5.0.6 on 2024-05-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shallyapp', '0003_sensordata_water'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='temp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
