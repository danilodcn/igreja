# Generated by Django 4.0.3 on 2022-04-04 23:18
# noqa
import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "Novo"),
                            (1, "Escrevendo"),
                            (2, "Aguardando revisão"),
                            (3, "Aguardando publicação"),
                            (3, "Publicado"),
                        ],
                        default=0,
                        verbose_name="Status",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Título"
                    ),
                ),
                (
                    "subtitle",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Subtítulo"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255, unique=True, verbose_name="Slug"
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
                    "document",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="",
                        verbose_name="Documento",
                    ),
                ),
                (
                    "content",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True, verbose_name="Conteúdo"
                    ),
                ),
                (
                    "meta_description",
                    models.CharField(blank=True, max_length=150),
                ),
                (
                    "publish_date",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="Data de publicação",
                    ),
                ),
                (
                    "review_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Data de revisão"
                    ),
                ),
                (
                    "published",
                    models.BooleanField(
                        default=False, verbose_name="Publicado"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="posts",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Autor",
                    ),
                ),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True,
                        related_name="posts",
                        to="blog.category",
                        verbose_name="Categorias",
                    ),
                ),
                (
                    "reviewed_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Revisado por",
                    ),
                ),
            ],
            options={
                "ordering": ["-publish_date"],
            },
        ),
    ]
