# Generated by Django 4.0.3 on 2022-05-29 19:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("church", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ministry",
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
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Descrição"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "church",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="church.church",
                        verbose_name="Igreja",
                    ),
                ),
                (
                    "leader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Líder",
                    ),
                ),
            ],
            options={
                "verbose_name": "Minstério",
                "verbose_name_plural": "Ministérios",
            },
        ),
    ]
