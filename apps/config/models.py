from ckeditor.fields import RichTextField
from django.db import models, transaction
from ordered_model.models import OrderedModel

from apps.church.models import Church, MemberType
from apps.core.models import Image


class ImageHome(Image):
    class Meta:
        ordering = ["order"]
        verbose_name = "Imagem da página principal"
        verbose_name = "Imagens da página principal"


class HomePageConfig(models.Model):
    title = models.CharField(
        "Título",
        max_length=200,
        help_text="título da página",
        null=False,
        blank=False,
    )

    church = models.ForeignKey(
        Church,
        on_delete=models.SET_NULL,
        help_text="Igreja ao qual a configuração estará associada",
        null=True,
        blank=True,
    )
    active = models.BooleanField("Ativa", default=False)
    content = RichTextField(verbose_name="Conteúdo", null=True, blank=True)

    body_title = models.CharField(
        "Subtítulo",
        max_length=200,
        help_text="Subtítulo da seção Pastores",
        null=True,
        blank=False,
    )

    body_content = RichTextField(
        verbose_name="Seção pastores", null=True, blank=True
    )

    maps_frame = models.TextField(
        verbose_name="Iframe do Google Maps", null=True, blank=True
    )
    # images = models.ManyToManyField(
    #     ImageHome, through='ImageHomeThroughModel', blank=True
    # )

    class Meta:
        verbose_name = "Condiguração da Principal"
        verbose_name_plural = "Configurações da Página Principal"

    @property
    def images(self):
        return ImageHomeThroughModel.objects.filter(homepageconfig_id=self.pk)

    def __str__(self):
        return "{} - {}".format(self.church or "", self.title or "sem título")

    def save(
        self,
        force_insert=None,
        force_update=None,
        using=None,
        update_fields=None,
    ) -> None:
        self.sure_only_active_church_home_config()
        self.sure_range_image_order()
        return super().save(force_insert, force_update, using, update_fields)

    def sure_only_active_church_home_config(self):
        qs = HomePageConfig.objects.filter(church=self.church, active=True)

        if self.active:
            qs.exclude(pk=self.pk).update(active=False)

    def sure_range_image_order(self):
        qs = self.images.all()
        with transaction.atomic():
            for i, image in enumerate(qs, start=1):
                image.order = i
                image.save()


class ImageHomeThroughModel(OrderedModel):
    imagehome = models.ForeignKey(ImageHome, on_delete=models.CASCADE)
    homepageconfig = models.ForeignKey(
        HomePageConfig, on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField("Ordem", null=True, blank=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    def __str__(self) -> str:
        name = self.imagehome.get_image_name()
        return "{} - {}".format(self.order, name)


class ChurchBodySection(OrderedModel):
    name = models.CharField(
        "Nome completo", max_length=100, null=True, blank=False
    )
    member_type = models.ForeignKey(
        MemberType,
        on_delete=models.SET_NULL,
        verbose_name="Tipo de membro",
        null=True,
        blank=True,
    )
    content = models.TextField("Texto", null=True, blank=True)
    image = models.ImageField("Imagem", null=True, blank=True)

    page = models.ForeignKey(
        HomePageConfig,
        on_delete=models.CASCADE,
        related_name="church_body_sections",
    )
    order_with_respect_to = "page"

    class Meta:
        ordering = (
            "page",
            "order",
        )

    def __str__(self) -> str:
        return "{} - {}".format(self.member_type or "Sem título", self.name)
