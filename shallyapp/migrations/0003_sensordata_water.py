# Generated by Django 5.0.6 on 2024-05-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shallyapp', '0002_waterlevel_alter_sensordata_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensordata',
            name='water',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
