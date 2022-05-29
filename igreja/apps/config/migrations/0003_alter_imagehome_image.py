# Generated by Django 4.0.3 on 2022-05-29 13:55

import image_optimizer.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0002_alter_imagehome_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagehome",
            name="image",
            field=image_optimizer.fields.OptimizedImageField(
                blank=True, null=True, upload_to="", verbose_name="Imagem"
            ),
        ),
    ]
