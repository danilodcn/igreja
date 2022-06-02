# Generated by Django 4.0.3 on 2022-06-02 01:52

import ckeditor_uploader.fields
import django.db.models.deletion
import image_optimizer.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("church", "0003_churchministry_remove_ministry_description_and_more"),
        ("financial", "0001_initial"),
        ("account", "0003_remove_profile_social_media_contactmeans_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                        max_length=50, unique=True, verbose_name="Nome"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=False, verbose_name="Ativo"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Event",
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
                        max_length=255, unique=True, verbose_name="Título"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255, unique=True, verbose_name="Slug"
                    ),
                ),
                (
                    "active",
                    models.BooleanField(default=False, verbose_name="Ativo"),
                ),
                (
                    "is_subscriptable",
                    models.BooleanField(verbose_name="Aceita inscrições"),
                ),
                ("initial_date", models.DateTimeField(verbose_name="Inicio")),
                ("end_date", models.DateTimeField(verbose_name="Inicio")),
                (
                    "image",
                    image_optimizer.fields.OptimizedImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="Imagem",
                    ),
                ),
                (
                    "resume",
                    models.TextField(
                        blank=True,
                        help_text="Breve resumo",
                        max_length=1000,
                        null=True,
                        verbose_name="Resumo",
                    ),
                ),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Conteúdo"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="account.address",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="events.category",
                    ),
                ),
                (
                    "church",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="church.church",
                    ),
                ),
            ],
            options={
                "verbose_name": "Evento",
                "verbose_name_plural": "Eventos",
                "ordering": ["initial_date"],
            },
        ),
        migrations.CreateModel(
            name="Subscription",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscriptions",
                        to="events.event",
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="financial.payment",
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="subscriptions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Inscrição",
                "verbose_name_plural": "Inscrições",
                "ordering": [],
            },
        ),
        migrations.CreateModel(
            name="EventPaymentOption",
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
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=20, verbose_name="Valor"
                    ),
                ),
                ("description", models.TextField(verbose_name="Descrição")),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="payment_options",
                        to="events.event",
                    ),
                ),
            ],
            options={
                "verbose_name": "Opção de pagamento do evento",
                "verbose_name_plural": "Opções de pagamento do evento",
                "ordering": ["order"],
            },
        ),
    ]
