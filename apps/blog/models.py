from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

from apps.account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    NEW = 0
    WRITING = 1
    AWAITING_FOR_REVIEW = 2
    AWAITING_FOR_PUBLISH = 3
    PUBLISHED = 3

    STATUS_CHOICES = (
        (NEW, "Novo"),
        (WRITING, "Escrevendo"),
        (AWAITING_FOR_REVIEW, "Aguardando revisão"),
        (AWAITING_FOR_PUBLISH, "Aguardando publicação"),
        (PUBLISHED, "Publicado"),
    )

    status = models.PositiveSmallIntegerField(
        verbose_name="Status", choices=STATUS_CHOICES, default=NEW
    )
    title = models.CharField(
        verbose_name="Título", max_length=255, unique=True
    )
    subtitle = models.CharField(
        verbose_name="Subtítulo", max_length=255, blank=True
    )
    slug = models.SlugField(verbose_name="Slug", max_length=255, unique=True)
    image = models.ImageField(verbose_name="Imagem", null=True, blank=True)
    document = models.FileField("Documento", null=True, blank=True)
    content = RichTextUploadingField(
        verbose_name="Conteúdo", null=True, blank=True
    )
    meta_description = models.CharField(max_length=150, blank=True)
    publish_date = models.DateTimeField(
        "Data de publicação", blank=True, null=True
    )
    review_date = models.DateTimeField(
        "Data de revisão", blank=True, null=True
    )
    published = models.BooleanField("Publicado", default=False)

    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Autor",
        related_name="posts",
        null=True,
        blank=True,
    )
    reviewed_by = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        verbose_name="Revisado por",
        related_name="reviews",
        null=True,
        blank=True,
    )
    categories = models.ManyToManyField(
        Category, related_name="posts", blank=True, verbose_name="Categorias"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish_date"]

    def __str__(self) -> str:
        return "Post - {}".format(self.title)
