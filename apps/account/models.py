from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import FieldTracker

from apps.account.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("Endereço de email", unique=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self):
        first_name = self.first_name.strip()
        last_name = self.last_name.strip()

        return "{} {}".format(first_name, last_name).strip()

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        self.on_create_user()
        return user

    def on_create_user(self):
        try:
            profile: Profile = self.profile

            if not profile.address:
                address = Address.objects.create()
                profile.address = address
                profile.save()

        except Profile.DoesNotExist:
            address = Address.objects.create()
            Profile.objects.create(user=self, address=address)


class Address(models.Model):
    STATE_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )

    ADDRESS_TYPE_CHOICES = (
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
    )

    class Meta:
        db_table = "core_address"
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    country = models.CharField(
        max_length=50,
        verbose_name="País",
        blank=True,
        null=True,
    )
    state = models.CharField(
        max_length=2,
        verbose_name="Estado",
        choices=[(v[0], v[0]) for v in STATE_CHOICES],
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        verbose_name="Cidade",
        blank=True,
        null=True,
    )
    zipcode = models.CharField(
        max_length=30,
        verbose_name="CEP",
        blank=True,
        null=True,
    )
    street = models.CharField(
        max_length=100,
        verbose_name="Rua",
        blank=True,
        null=True,
    )
    complement = models.CharField(
        max_length=100,
        verbose_name="Complemento",
        blank=True,
        null=True,
    )
    number = models.CharField(
        max_length=30,
        verbose_name="Número",
        blank=True,
        null=True,
    )
    neighborhood = models.CharField(
        max_length=100,
        verbose_name="Bairro",
        blank=True,
        null=True,
    )
    address_type = models.CharField(
        max_length=100,
        choices=ADDRESS_TYPE_CHOICES,
        verbose_name="Tipo de endereço",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        default = "---"
        return "{}, {}, {}/{}".format(
            self.street or default,
            self.number or default,
            self.city or default,
            self.get_state_display() or default,
        )


class Profile(models.Model):
    GENDER_CHOICES = (
        (0, "Homem"),
        (1, "Mulher"),
        (2, "-"),
    )

    PHONE_CHOICES = (
        ("residential", "RESIDENCIAL"),
        ("commercial", "COMERCIAL"),
        ("cellphone", "CELULAR"),
    )

    MARITAL_STATUS_CHOICES = (
        ("single", "SOLTEIRO"),
        ("married", "CASADO"),
        ("widower", "VIUVO"),
        ("divorced", "DIVORCIADO"),
    )

    tracker = FieldTracker()
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="profile",
        blank=True,
        null=True,
    )

    address = models.OneToOneField(
        Address,
        models.CASCADE,
        related_name="profile",
        null=True,
        blank=True,
    )

    gender = models.IntegerField(
        verbose_name="Sexo",
        choices=GENDER_CHOICES,
        default=2,
        blank=True,
        null=True,
    )

    cpf = models.CharField(
        max_length=14,
        verbose_name="CPF",
        blank=True,
        null=True,
    )
    cnh = models.CharField(
        max_length=14,
        verbose_name="CNH",
        blank=True,
        null=True,
    )
    rg = models.CharField(
        max_length=40,
        verbose_name="RG",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=17,
        verbose_name="Telefone",
        blank=True,
        null=True,
    )
    income_bracket = models.CharField(
        max_length=200,
        verbose_name="Faixa de renda",
        blank=True,
        null=True,
    )
    occupation = models.CharField(
        max_length=100,
        verbose_name="Profissão",
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Data de Nascimento",
    )
    phone_type = models.CharField(
        max_length=100,
        choices=PHONE_CHOICES,
        verbose_name="Tipo de Telefone",
        blank=True,
        null=True,
    )
    marital_status = models.CharField(
        max_length=100,
        choices=MARITAL_STATUS_CHOICES,
        verbose_name="Estado Civil",
        blank=True,
        null=True,
    )
    emitting_organ = models.CharField(
        max_length=100,
        verbose_name="Orgão Emissor",
        blank=True,
        null=True,
    )
    expedition_date = models.DateField(
        verbose_name="Data de Expedição",
        blank=True,
        null=True,
    )
    email_message_enabled = models.BooleanField(
        verbose_name="Aceitar e-mails para comunicação?",
        default=False,
    )
    phone_message_enabled = models.BooleanField(
        verbose_name="Aceitar comunicação de celular",
        default=False,
    )
    is_main_contact = models.BooleanField(
        verbose_name="É o contato principal",
        default=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "account_profile"
        verbose_name = "Informação Pessoal"
        verbose_name_plural = "Informações Pessoais"

    def __str__(self):
        if self.user:
            return str(self.user)
        return "Usuário não associado"
