# Generated by Django 4.0.3 on 2022-03-30 01:04

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                    "password",
                    models.CharField(max_length=128, verbose_name="password"),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        verbose_name="email address",
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Address",
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
                    "country",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Country",
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AC", "AC"),
                            ("AL", "AL"),
                            ("AP", "AP"),
                            ("AM", "AM"),
                            ("BA", "BA"),
                            ("CE", "CE"),
                            ("DF", "DF"),
                            ("ES", "ES"),
                            ("GO", "GO"),
                            ("MA", "MA"),
                            ("MT", "MT"),
                            ("MS", "MS"),
                            ("MG", "MG"),
                            ("PA", "PA"),
                            ("PB", "PB"),
                            ("PR", "PR"),
                            ("PE", "PE"),
                            ("PI", "PI"),
                            ("RJ", "RJ"),
                            ("RN", "RN"),
                            ("RS", "RS"),
                            ("RO", "RO"),
                            ("RR", "RR"),
                            ("SC", "SC"),
                            ("SP", "SP"),
                            ("SE", "SE"),
                            ("TO", "TO"),
                        ],
                        max_length=2,
                        null=True,
                        verbose_name="State",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="City",
                    ),
                ),
                (
                    "zipcode",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Zip Code",
                    ),
                ),
                (
                    "street",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Street",
                    ),
                ),
                (
                    "complement",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Complement",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="Number",
                    ),
                ),
                (
                    "neighborhood",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Neighborhood",
                    ),
                ),
                (
                    "address_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("alameda", "ALAMEDA"),
                            ("avenida", "AVENIDA"),
                            ("chacara", "CHACARA"),
                            ("condominio", "CONDOMÍNIO"),
                            ("conjunto", "CONJUNTO"),
                            ("estrada", "ESTRADA"),
                            ("ladeira", "LADEIRA"),
                            ("largo", "LARGO"),
                            ("parque", "PARQUE"),
                            ("praca", "PRAÇA"),
                            ("praia", "PRAIA"),
                            ("quadra", "QUADRA"),
                            ("rodovia", "RODOVIA"),
                            ("rua", "RUA"),
                            ("travessa", "TRAVESSA"),
                            ("via", "VIA"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Address Type",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
                "db_table": "core_address",
            },
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "gender",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "Male"), (1, "Female"), (2, "-")],
                        default=2,
                        null=True,
                        verbose_name="Sexo",
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        blank=True,
                        max_length=14,
                        null=True,
                        verbose_name="CPF",
                    ),
                ),
                (
                    "cnh",
                    models.CharField(
                        blank=True,
                        max_length=14,
                        null=True,
                        verbose_name="CNH",
                    ),
                ),
                (
                    "rg",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="RG"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        null=True,
                        verbose_name="Phone",
                    ),
                ),
                (
                    "income_bracket",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Faixa de renda",
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Profissão",
                    ),
                ),
                (
                    "birth_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        verbose_name="Data de Nascimento",
                    ),
                ),
                (
                    "phone_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("residential", "RESIDENCIAL"),
                            ("commercial", "COMERCIAL"),
                            ("cellphone", "CELULAR"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Tipo de Telefone",
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("single", "SOLTEIRO"),
                            ("married", "CASADO"),
                            ("widower", "VIUVO"),
                            ("divorced", "DIVORCIADO"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Estado Civil",
                    ),
                ),
                (
                    "emitting_organ",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Orgão Emissor",
                    ),
                ),
                (
                    "expedition_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de Expedição"
                    ),
                ),
                (
                    "email_message_enabled",
                    models.BooleanField(
                        default=False,
                        verbose_name="Aceitar e-mails para comunicação?",
                    ),
                ),
                (
                    "phone_message_enabled",
                    models.BooleanField(
                        default=False,
                        verbose_name="Aceitar comunicação de celular",
                    ),
                ),
                (
                    "is_main_contact",
                    models.BooleanField(
                        default=False, verbose_name="Is Main Contact"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "address",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to="account.address",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Informação Pessoal",
                "verbose_name_plural": "Informações Pessoais",
                "db_table": "account_profile",
            },
        ),
    ]
