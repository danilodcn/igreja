from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from image_optimizer.fields import OptimizedImageField
from ordered_model.models import OrderedModel

from igreja.apps.account.models import Address, CustomUser
from igreja.apps.church.models import Church
from igreja.apps.financial.models import Payment


class Category(OrderedModel):
    name = models.CharField("Nome", max_length=50, unique=True)

    active = models.BooleanField("Ativo", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["order"]


class Event(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=255, unique=True
    )
    slug = models.SlugField(verbose_name="Slug", max_length=255, unique=True)

    active = models.BooleanField("Ativo", default=False)
    is_subscriptable = models.BooleanField("Aceita inscrições")

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Categoria",
        null=True,
        blank=False,
    )
    initial_date = models.DateTimeField(verbose_name="Inicio")
    end_date = models.DateTimeField(verbose_name="Fim")
    church = models.ForeignKey(
        to=Church,
        on_delete=models.SET_NULL,
        verbose_name="Igreja",
        null=True,
        blank=False,
    )
    address = models.ForeignKey(
        to=Address,
        on_delete=models.SET_NULL,
        verbose_name="Endereço",
        null=True,
        blank=True,
    )
    image = OptimizedImageField(
        verbose_name="Imagem",
        optimized_image_resize_method="cover",
        null=True,
        blank=True,
    )
    resume = models.TextField(
        "Resumo",
        max_length=1000,
        help_text="Breve resumo",
        null=True,
        blank=True,
    )
    content = RichTextUploadingField(
        verbose_name="Conteúdo", null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ["initial_date"]


class EventPaymentOption(OrderedModel):
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, related_name="payment_options"
    )
    amount = models.DecimalField("Valor", max_digits=20, decimal_places=2)
    max_installment = models.PositiveIntegerField(
        "Numero máximo de parcelas", null=True, blank=True
    )
    description = models.TextField("Descrição")

    class Meta:
        verbose_name = "Opção de pagamento do evento"
        verbose_name_plural = "Opções de pagamento do evento"
        ordering = ["order"]


class Subscription(models.Model):
    event = models.ForeignKey(
        to=Event,
        on_delete=models.CASCADE,
        related_name="subscriptions",
        verbose_name="Evento",
    )
    payment = models.ForeignKey(
        Payment,
        on_delete=models.SET_NULL,
        verbose_name="Pagamento",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        verbose_name="Usuário",
        to=CustomUser,
        on_delete=models.SET_NULL,
        related_name="subscriptions",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        verbose_name="Atualizado por",
        to=CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        ordering = []
