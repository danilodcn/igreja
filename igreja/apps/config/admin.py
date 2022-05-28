from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from ordered_model.admin import (
    OrderedInlineModelAdminMixin,
    OrderedStackedInline,
    OrderedTabularInline,
)

from igreja.apps.core import filters

from .models import (
    ChurchBodySection,
    HomePageConfig,
    ImageHome,
    ImageHomeThroughModel,
    PageContent,
)


class ImageHomeAdmin(admin.ModelAdmin):
    search_fields = ["name", "image"]


class PastorConfigInlineForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = HomePageConfig
        fields = "__all__"


class PastorConfigInlineAdmin(OrderedTabularInline):
    form = PastorConfigInlineForm
    model = ChurchBodySection
    extra = 0
    readonly_fields = (
        "order",
        "move_up_down_links",
        "get_image",
    )
    ordering = ("order",)
    fields = ["move_up_down_links", "name", "member_type", "content", "image"]

    def get_fieldsets(self, request: HttpRequest, obj):
        fields = (
            (
                None,
                {
                    "fields": [
                        "move_up_down_links",
                        ("name", "member_type"),
                        "content",
                        "image",
                        "get_image",
                    ]
                },
            ),
        )
        return fields

    @admin.display(description="imagem")
    def get_image(self, obj=None):
        if obj:
            html = """<img src={} height="200">""".format(obj.image.url)
            return mark_safe(html)


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageHomeThroughModel
        exclude = []

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


class ImagesHeaderHomePageInlineAdmin(OrderedStackedInline):
    model = ImageHomeThroughModel
    # model.__str__ = lambda _: ""
    # model._meta.verbose_name = "imagem"
    # model._meta.verbose_name_plural = "imagens"
    form = ImageForm
    extra = 0
    autocomplete_fields = ["imagehome"]
    readonly_fields = [
        "get_image",
    ]
    fields = ["imagehome", "order"]

    @admin.display(description="imagem")
    def get_image(self, obj=None):
        if obj:
            html = """<img src={} height="200">""".format(
                obj.imagehome.image.url
            )
            return mark_safe(html)

    def get_fieldsets(self, request, obj):
        return ((None, {"fields": [("imagehome", "order"), "get_image"]}),)


class PageContentAdminForm(forms.ModelForm):
    content = forms.CharField(label="Conteúdo", widget=CKEditorWidget())

    class Meta:
        model = PageContent
        fields = "__all__"


class PageContentInlineAdmin(admin.TabularInline):
    model = PageContent
    form = PageContentAdminForm


class HomePageConfigForm(forms.ModelForm):
    class Meta:
        model = HomePageConfig
        fields = "__all__"


class HomePageConfigAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ["__str__", "active"]
    form = HomePageConfigForm

    inlines = [
        ImagesHeaderHomePageInlineAdmin,
        PastorConfigInlineAdmin,
        PageContentInlineAdmin,
    ]
    exclude = ["images"]
    list_filter = [
        filters.ChurchFilter,
        ("church__address__state", admin.AllValuesFieldListFilter),
    ]
    readonly_fields = [
        "get_frame_maps",
    ]

    @admin.display(description="Localização")
    def get_frame_maps(self, obj: HomePageConfig):
        if obj.maps_frame:
            return mark_safe(obj.maps_frame)
        return " - "


admin.site.register(HomePageConfig, HomePageConfigAdmin)
admin.site.register(ImageHome, ImageHomeAdmin)
