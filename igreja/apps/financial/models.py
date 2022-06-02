from django.db import models
from model_utils import FieldTracker


class Payment(models.Model):
    CREDIT = 0
    DEBIT = 1
    PAYMENT_SLIP = 2
    BANK_SLIP = 3
    PAYMENT_TYPE_CHOICES = (
        (CREDIT, "Crédito"),
        (DEBIT, "Débito"),
        (PAYMENT_SLIP, "Depósito"),
        (BANK_SLIP, "Boleto"),
    )

    VISA = 1
    MASTERCARD = 2
    ELO = 3
    AMEX = 4
    CABAL = 5
    HIPERCARD = 6
    PAYMENT_SLIP_BRAND = 7
    UNKNOWN = 8
    BRAND_CHOICES = (
        (VISA, "Visa"),
        (MASTERCARD, "Mastercard"),
        (ELO, "Elo"),
        (AMEX, "Amex"),
        (CABAL, "Cabal"),
        (HIPERCARD, "Hipercard"),
        (PAYMENT_SLIP_BRAND, "Depósito"),
        (UNKNOWN, "Desconhecido"),
    )

    EVENT = 0
    STORE = 1

    LOCATION_TYPE_CHOICES = (
        (EVENT, "Evento"),
        (STORE, "Loja"),
    )

    type = models.IntegerField(
        "Tipo de pagamento", choices=PAYMENT_TYPE_CHOICES, default=CREDIT
    )
    location_type = models.IntegerField(
        "Tipo local", choices=LOCATION_TYPE_CHOICES
    )
    brand = models.IntegerField("Bandeira", choices=BRAND_CHOICES)

    amount = models.DecimalField("Valor", max_digits=20, decimal_places=2)

    number_of_installments = models.IntegerField(
        "Quantidade de parcelas", null=True, blank=True
    )
    date_of_payment = models.DateTimeField("Data de pagamento", null=True)

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

    def get_brand_type(self, brand: str):
        brand = brand.lower()
        for type, brand_name in self.BRAND_CHOICES:
            if brand_name.lower() == brand:
                return type

        return self.UNKNOWN


class Installment(models.Model):
    def __str__(self):
        return "Parcela - {:06d}".format(self.pk)

    class Meta:
        verbose_name = "Parcela"
        verbose_name_plural = "Parcelas"

    payment = models.ForeignKey(
        Payment, related_name="installments", on_delete=models.CASCADE
    )

    payment_date = models.DateField(
        verbose_name="Data pagamento", default=None, null=True
    )

    amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        verbose_name="Valor",
        blank=True,
        null=True,
    )

    tax_value = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        verbose_name="Taxa",
        blank=True,
        null=True,
    )
    week = models.IntegerField(verbose_name="Semana", blank=True, null=True)
    sequence = models.IntegerField(verbose_name="Sequência", default=0)
