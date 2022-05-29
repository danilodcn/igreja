from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from ordered_model.admin import (
    OrderedInlineModelAdminMixin,
    OrderedStackedInline,
)

from igreja.apps.core import filters

from .models import (
    ChurchBodySection,
    ImageHome,
    ImageThroughModel,
    MinistryChurchSection,
    MinistryPageConfig,
    PageConfig,
    PageContent,
)


class ImageHomeAdmin(admin.ModelAdmin):
    search_fields = ["name", "image"]

    def has_module_permission(self, request: HttpRequest) -> bool:
        return False


class BodyConfigInlineForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PageConfig
        fields = "__all__"


class BodyConfigInlineAdmin(OrderedStackedInline):
    model = ChurchBodySection
    extra = 0
    readonly_fields = (
        "order",
        "move_up_down_links",
        "get_image",
    )
    ordering = ("order",)
    fields_that_contain_diferences = ["member_type"]
    fields = ["move_up_down_links", "name", "content", "image"]

    def get_fields(self, request: HttpRequest, obj=...):
        return set(self.fields).union(self.fields_that_contain_diferences)

    def get_fieldsets(self, request: HttpRequest, obj=...):
        fields = (
            (
                None,
                {
                    "fields": [
                        (
                            "name",
                            *self.fields_that_contain_diferences,
                            "move_up_down_links",
                        ),
                        ("content",),
                        (
                            "image",
                            "get_image",
                        ),
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


class MinsterConfigSectionAdminInline(BodyConfigInlineAdmin):
    model = MinistryChurchSection
    fields_that_contain_diferences = ["ministry"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageThroughModel
        exclude = []

    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)


class ImagesHeaderHomePageInlineAdmin(OrderedStackedInline):
    model = ImageThroughModel
    form = ImageForm
    extra = 0
    autocomplete_fields = ["image"]
    readonly_fields = [
        "get_image",
    ]
    fields = ["image", "order"]

    @admin.display(description="imagem")
    def get_image(self, obj: ImageThroughModel = None):
        if obj:
            html = """<img src={} height="200">""".format(obj.image.image.url)
            return mark_safe(html)

    def get_fieldsets(self, request, obj):
        return ((None, {"fields": [("image", "order"), "get_image"]}),)


class PageContentAdminForm(forms.ModelForm):
    content = forms.CharField(label="Conteúdo", widget=CKEditorWidget())

    class Meta:
        model = PageContent
        fields = "__all__"


class PageContentInlineAdmin(admin.StackedInline):
    model = PageContent
    form = PageContentAdminForm
    extra = 0

    fieldsets = [
        (
            None,
            {
                "fields": (
                    ("title", "section"),
                    ("content"),
                )
            },
        )
    ]


class PageConfigForm(forms.ModelForm):
    class Meta:
        model = PageConfig
        fields = "__all__"


class PageConfigAdmin(OrderedInlineModelAdminMixin, admin.ModelAdmin):
    list_display = ["__str__", "church", "active"]
    form = PageConfigForm
    inlines = [
        PageContentInlineAdmin,
        ImagesHeaderHomePageInlineAdmin,
        BodyConfigInlineAdmin,
    ]
    exclude = ["images"]
    list_filter = [
        filters.ChurchFilter,
        ("church__address__state", admin.AllValuesFieldListFilter),
    ]
    page_type = PageConfig.INDEX

    def get_readonly_fields(self, request: HttpRequest, obj: PageConfig):
        if obj and obj.type == PageConfig.INDEX:
            return [
                "get_frame_maps",
            ]
        else:
            return []

    @admin.display(description="Localização")
    def get_frame_maps(self, obj: PageConfig):
        if obj.maps_frame:
            return mark_safe(obj.maps_frame)
        return " - "

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).filter(type=self.page_type)


class MinistryPageConfigAdmin(PageConfigAdmin):
    inlines = [
        PageContentInlineAdmin,
        ImagesHeaderHomePageInlineAdmin,
    ]
    exclude = ["get_frame_maps", "maps_frame"]
    page_type = PageConfig.MINISTRY


admin.site.register(PageConfig, PageConfigAdmin)
admin.site.register(MinistryPageConfig, MinistryPageConfigAdmin)
admin.site.register(ImageHome, ImageHomeAdmin)
