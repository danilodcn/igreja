# Generated by Django 4.0.3 on 2022-04-09 19:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("account", "0004_customuser_username"),
    ]

    operations = [
        migrations.CreateModel(
            name="Church",
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
                        help_text="Nome da igreja",
                        max_length=100,
                        verbose_name="Nome",
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="Usado para identificar a igreja",
                        max_length=30,
                        unique=True,
                        verbose_name="Código",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "address",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.address",
                        verbose_name="Endereço",
                    ),
                ),
            ],
            options={
                "verbose_name": "Igreja",
                "verbose_name_plural": "Igrejas",
            },
        ),
        migrations.CreateModel(
            name="MemberType",
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
                (
                    "code",
                    models.CharField(
                        help_text="Usado para identificar o tipo de membro",
                        max_length=30,
                        unique=True,
                        verbose_name="Código",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Tipo de membro",
                "verbose_name_plural": "Tipos de membros",
                "db_table": "church_member_type",
            },
        ),
        migrations.CreateModel(
            name="Member",
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
                    "church",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="members",
                        to="church.church",
                        verbose_name="Igreja",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="member",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Membro",
                    ),
                ),
                (
                    "member_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="church.membertype",
                        verbose_name="Tipo de membro",
                    ),
                ),
            ],
            options={
                "verbose_name": "Membro",
                "verbose_name_plural": "Membros",
            },
        ),
    ]
