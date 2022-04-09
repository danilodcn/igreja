from django.db import models
from ordered_model.models import OrderedModel

from apps.account.models import Address, CustomUser


class MemberType(OrderedModel):
    name = models.CharField("Nome", max_length=100, null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    code = models.CharField(
        "Código",
        max_length=30,
        unique=True,
        help_text="Usado para identificar o tipo de membro",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "church_member_type"
        verbose_name = "Tipo de membro"
        verbose_name_plural = "Tipos de membros"

    def __str__(self) -> str:
        return self.name or " - "


class Church(models.Model):
    name = models.CharField("Nome", max_length=100, help_text="Nome da igreja")
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name="Endereço",
        null=True,
        blank=True,
    )
    code = models.CharField(
        "Código",
        max_length=30,
        unique=True,
        help_text="Usado para identificar a igreja",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Igreja"
        verbose_name_plural = "Igrejas"

    def __str__(self) -> str:
        return self.name or " - "


class Member(models.Model):
    member = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Membro",
        related_name="member",
    )
    member_type = models.ForeignKey(
        MemberType, on_delete=models.CASCADE, verbose_name="Tipo de membro"
    )

    church = models.ForeignKey(
        Church,
        on_delete=models.CASCADE,
        verbose_name="Igreja",
        related_name="members",
    )

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"
