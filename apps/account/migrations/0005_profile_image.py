# Generated by Django 4.0.3 on 2022-04-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_customuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Perfil"
            ),
        ),
    ]