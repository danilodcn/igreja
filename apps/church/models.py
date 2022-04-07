from django.db import models

from apps.account.models import Address, CustomUser


class MembrerType(models.Model):
    class Meta:
        verbose_name = "Tipo de membro"
        verbose_name_plural = "Tipos de membros"


class Church(models.Model):
    name = models.CharField("Nome", max_length=100, help_text="Nome da igreja")
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, null=True, blank=True
    )
    leaders = models.ManyToManyField(CustomUser, "Líderes")
