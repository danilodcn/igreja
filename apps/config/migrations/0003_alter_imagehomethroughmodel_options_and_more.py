# Generated by Django 4.0.3 on 2022-04-09 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0002_alter_imagehome_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="imagehomethroughmodel",
            options={
                "ordering": ["order"],
                "verbose_name": "Imagem",
                "verbose_name_plural": "Imagens",
            },
        ),
        migrations.RemoveField(
            model_name="homepageconfig",
            name="images",
        ),
        migrations.AlterField(
            model_name="imagehome",
            name="order",
            field=models.PositiveIntegerField(
                db_index=True, editable=False, null=True, verbose_name="Ordem"
            ),
        ),
    ]
