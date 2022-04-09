from django.db import models
from ordered_model.models import OrderedModel


class Image(models.Model):
    name = models.CharField("Nome", max_length=100, null=True, blank=True)
    image = models.ImageField("Imagem", null=True, blank=True)
    order = models.PositiveIntegerField("Ordem", null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.pk} - {self.name or self.image}"
