from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ordered_model.models import OrderedModel


class ModelBase(OrderedModel):
    name = models.CharField("Nome", max_length=250)
    active = models.BooleanField("Ativo", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("order",)

    def __str__(self) -> str:
        return f"{self.name} - {self.order}"


class SectionBase(ModelBase):
    content = models.ForeignKey(
        "Content",
        verbose_name="para o conteudo",
        on_delete=models.CASCADE,
        related_name="content",
        help_text="Conteudo base",
        null=False,
        blank=False,
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return super().__str__()


class ContenSection(SectionBase):
    content = RichTextUploadingField(
        verbose_name="Conteúdo",
        help_text="Conteúdo principal",
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

    class Meta:
        verbose_name = "Seção Conteúdo"
        verbose_name_plural = "Seção Conteúdos"
        ordering = ["order"]


class ImageSection(SectionBase):
    ...


class Content(ModelBase):
    ...
