from django.db import models
from image_optimizer.fields import OptimizedImageField
from ordered_model.models import OrderedModel


class Image(models.Model):
    name = models.CharField("Nome", max_length=100, null=True, blank=True)
    image = OptimizedImageField(
        verbose_name="Imagem",
        optimized_image_resize_method="cover",
        null=True,
        blank=True,
    )
    order = models.PositiveIntegerField("Ordem", null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        name = self.get_image_name()
        return f"{self.pk} - {name}"

    def get_image_name(self):
        return f"{self.name or self.image}"
