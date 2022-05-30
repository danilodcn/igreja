from ckeditor.fields import RichTextField
from django.db import models, transaction
from ordered_model.models import OrderedModel

from igreja.apps.church.models import Church, MemberType, Ministry
from igreja.apps.core.models import Image


class ImageHome(Image):
    class Meta:
        ordering = ["order"]
        verbose_name = "Imagem da página"
        verbose_name = "Imagens das páginas"


class PageConfig(models.Model):
    INDEX = 1
    MINISTRY = 2
    PAGE_TYPES = (
        (INDEX, "Página principal"),
        (MINISTRY, "Ministérios"),
    )
    type = models.PositiveSmallIntegerField(
        "Tipo de página",
        choices=PAGE_TYPES,
        help_text="Tipo de página",
    )
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
        verbose_name="Igreja",
        help_text="Igreja ao qual a configuração estará associada",
        related_name="home_config",
        null=True,
        blank=True,
    )
    active = models.BooleanField("Ativa", default=False)
    maps_frame = models.TextField(
        verbose_name="Iframe do Google Maps", null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return "{} - {} - {}".format(
            self.pk,
            self.church or "Nenhuma igreja cadastrada",
            self.title,
        )

    @property
    def images(self):
        return ImageThroughModel.objects.filter(page_id=self.pk)

    @property
    def content(self):
        return PageContent.objects.filter(page_id=self.pk)

    @property
    def body_page_sections(self):
        return ChurchBodySection.objects.filter(page_id=self.pk)

    @property
    def ministry_page_sections(self):
        return MinistryChurchSection.objects.filter(page_id=self.pk)

    def save(
        self,
        force_insert=None,
        force_update=None,
        using=None,
        update_fields=None,
    ) -> None:
        self.sure_only_active_church_home_config()
        # self.sure_range_image_order()
        self.sure_in_order(self.images, "order")
        self.sure_in_order(self.content, "section")
        return super().save(force_insert, force_update, using, update_fields)

    def sure_only_active_church_home_config(self):
        qs = PageConfig.objects.filter(church=self.church, active=True)

        if self.active:
            qs.exclude(pk=self.pk).update(active=False)

    def sure_in_order(self, qs: models.QuerySet, field: str):
        with transaction.atomic():
            for i, obj in enumerate(qs, start=1):
                setattr(obj, field, i)
                obj.save()


class PageContent(models.Model):
    section = models.PositiveSmallIntegerField(
        "Número da seção",
        help_text="As seções serão apresentadas em ordem decrescente",
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
        PageConfig,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Conteúdo da Página"
        verbose_name_plural = "Conteúdos da Página"
        ordering = ["section"]

    def __str__(self) -> str:
        return "{} - {}".format(self.section, self.title)


class ImageThroughModel(OrderedModel):
    image = models.ForeignKey(ImageHome, on_delete=models.CASCADE)
    page = models.ForeignKey(PageConfig, on_delete=models.CASCADE)
    order = models.PositiveIntegerField("Ordem", null=True, blank=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"

    def __str__(self) -> str:
        name = self.image.get_image_name()
        return "{} - {}".format(self.order, name)


class ChurchMinistryAdnBodySection(OrderedModel):
    name = models.CharField(
        "Nome completo", max_length=100, null=True, blank=False
    )
    image = models.ImageField("Imagem", null=True, blank=True)
    content = models.TextField("Texto", null=True, blank=True)

    page = models.ForeignKey(
        PageConfig,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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

    class Meta:
        ordering = (
            "page",
            "order",
        )
        verbose_name = "Membro da Igreja"
        verbose_name_plural = "Seções dos Membros da Igreja"

    def __str__(self) -> str:
        return "{} - {}".format(self.member_type or "Sem título", self.name)


class MinistryChurchSection(ChurchMinistryAdnBodySection):
    ministry = models.ForeignKey(
        Ministry,
        on_delete=models.SET_NULL,
        verbose_name="Ministério",
        null=True,
        blank=False,
    )

    class Meta:
        ordering = (
            "page",
            "order",
        )
        verbose_name = "Ministério da Igreja"
        verbose_name_plural = "Seções dos Ministérios da Igreja"
