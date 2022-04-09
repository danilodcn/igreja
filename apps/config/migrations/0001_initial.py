# Generated by Django 4.0.3 on 2022-04-09 18:02

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("church", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePageConfig",
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
                    "title",
                    models.CharField(
                        help_text="título da página",
                        max_length=200,
                        verbose_name="Título",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=False, verbose_name="Ativa"),
                ),
                (
                    "content",
                    ckeditor.fields.RichTextField(
                        blank=True, null=True, verbose_name="Conteúdo"
                    ),
                ),
                (
                    "maps_frame",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Iframe do Google Maps",
                    ),
                ),
                (
                    "church",
                    models.ForeignKey(
                        blank=True,
                        help_text="Igreja ao qual a configuração estará associada",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="church.church",
                    ),
                ),
            ],
            options={
                "verbose_name": "Condiguração da Home",
                "verbose_name_plural": "Configurações da Página Home",
            },
        ),
        migrations.CreateModel(
            name="ImageHome",
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
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Nome",
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
                    "order",
                    models.PositiveIntegerField(
                        db_index=True,
                        editable=False,
                        null=True,
                        verbose_name="Ordem",
                    ),
                ),
            ],
            options={
                "verbose_name": "Imagens da Home",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="PastorSection",
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
                (
                    "page",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pastor_sections",
                        to="config.homepageconfig",
                    ),
                ),
            ],
            options={
                "ordering": ("page", "order"),
            },
        ),
        migrations.CreateModel(
            name="ImageHomeThroughModel",
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
                        blank=True, null=True, verbose_name="Ordem"
                    ),
                ),
                (
                    "homepageconfig",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="config.homepageconfig",
                    ),
                ),
                (
                    "imagehome",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="config.imagehome",
                    ),
                ),
            ],
            options={
                "verbose_name": "Imagem",
                "verbose_name_plural": "Imagens",
                "ordering": ["order"],
            },
        ),
    ]
