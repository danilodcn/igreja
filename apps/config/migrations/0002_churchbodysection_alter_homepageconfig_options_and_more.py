# Generated by Django 4.0.3 on 2022-05-08 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("church", "0001_initial"),
        ("config", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChurchBodySection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, null=True, verbose_name="Nome completo"
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True, null=True, verbose_name="Texto"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="Imagem",
                    ),
                ),
                (
                    "member_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="church.membertype",
                        verbose_name="Tipo de membro",
                    ),
                ),
            ],
            options={
                "ordering": ("page", "order"),
            },
        ),
        migrations.AlterModelOptions(
            name="homepageconfig",
            options={
                "verbose_name": "Condiguração da Principal",
                "verbose_name_plural": "Configurações da Página Principal",
            },
        ),
        migrations.AlterModelOptions(
            name="imagehome",
            options={
                "ordering": ["order"],
                "verbose_name": "Imagens da página principal",
            },
        ),
        migrations.DeleteModel(
            name="PastorSection",
        ),
        migrations.AddField(
            model_name="churchbodysection",
            name="page",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="church_body_sections",
                to="config.homepageconfig",
            ),
        ),
    ]