from ckeditor.fields import RichTextField
from django.db import models, transaction
from ordered_model.models import OrderedModel

from igreja.apps.church.models import Church, MemberType
from igreja.apps.core.models import Image


class ImageHome(Image):
    class Meta:
        ordering = ["order"]
        verbose_name = "Imagem da página principal"
        verbose_name = "Imagens da página principal"


class HomePageConfig(models.Model):
    church = models.ForeignKey(
        Church,
        on_delete=models.SET_NULL,
        help_text="Igreja ao qual a configuração estará associada",
        related_name="home_config",
        null=True,
        blank=True,
    )
    active = models.BooleanField("Ativa", default=False)

    maps_frame = models.TextField(
        verbose_name="Iframe do Google Maps", null=True, blank=True
    )
    # images = models.ManyToManyField(
    #     ImageHome, through='ImageHomeThroughModel', blank=True
    # )

    class Meta:
        verbose_name = "Configuração da Página Principal"
        verbose_name_plural = "Configurações da Página Principal"

    def __str__(self):
        return "{} - {}".format(
            self.pk, self.church or "Nenhuma igreja cadastrada"
        )

    @property
    def images(self):
        return ImageHomeThroughModel.objects.filter(homepageconfig_id=self.pk)

    @property
    def church_body_sections(self):
        return ChurchBodySection.objects.filter(page_id=self.pk)

    @property
    def page_content_index(self):
        return PageContent.objects.filter(
            page_id=self.pk, page_type=PageContent.INDEX
        )

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


class PageContent(models.Model):
    INDEX = 1
    MINISTRY = 2
    PAGE_TYPES = (
        (INDEX, "Página principal"),
        (MINISTRY, "Ministérios"),
    )

    BODY_SECTIONS = 10
    MINISTRY_SECTIONS = 11
    SECTIONS_TYPES = (
        (BODY_SECTIONS, "Seção dos pastores"),
        (MINISTRY_SECTIONS, "Seção dos ministérios"),
    )

    page_type = models.PositiveSmallIntegerField(
        "Tipo de página",
        choices=PAGE_TYPES,
        help_text="Tipo de página",
    )
    content_type = models.PositiveSmallIntegerField(
        "Tipo de conteúdo",
        choices=SECTIONS_TYPES,
        help_text="Tipo de conteúdo",
    )
    title = models.CharField(
        "Título",
        max_length=200,
        help_text="título do conteúdo",
        null=False,
        blank=False,
    )
    content = RichTextField(verbose_name="Conteúdo", null=True, blank=True)
    page = models.ForeignKey(
        HomePageConfig,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Conteúdo da Página"
        verbose_name_plural = "Conteúdos da Página"


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


class ChurchMinistryAdnBodySection(OrderedModel):
    name = models.CharField(
        "Nome completo", max_length=100, null=True, blank=False
    )
    image = models.ImageField("Imagem", null=True, blank=True)
    content = models.TextField("Texto", null=True, blank=True)

    page = models.ForeignKey(
        HomePageConfig,
        on_delete=models.CASCADE,
    )

    order_with_respect_to = "page"

    class Meta:
        ordering = (
            "page",
            "order",
        )
        abstract = True


class ChurchBodySection(ChurchMinistryAdnBodySection):
    member_type = models.ForeignKey(
        MemberType,
        on_delete=models.SET_NULL,
        verbose_name="Tipo de membro",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return "{} - {}".format(self.member_type or "Sem título", self.name)


class MinistryChurch(ChurchMinistryAdnBodySection):
    ...


class ContactMeans(models.Model):
    WHATSAPP = "whatsapp"
    EMAIL = "email"
    FACEBOOK = "facebook"
    TYPES = (
        (WHATSAPP, WHATSAPP),
        (EMAIL, EMAIL),
        (FACEBOOK, FACEBOOK),
    )
    type = models.CharField("Forma de contato", choices=TYPES, max_length=30)
    contact = models.CharField("Contato", max_length=200)

    ministry = models.ForeignKey(to=MinistryChurch, on_delete=models.CASCADE)
