# Generated by Django 4.0.3 on 2022-04-09 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_address_maps_frame"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="maps_frame",
        ),
    ]
