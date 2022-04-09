from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils import timezone
from ordered_model.admin import OrderedModelAdmin

from .models import Category, Post, Reviews


class PostsInline(admin.TabularInline):
    model = Post.categories.through
    # template = "blog/inline/tabular.html"
    readonly_fields = ["post", "get_status", "get_published", "get_author"]
    autocomplete_fields = [
        "post",
    ]
    extra = 0
    verbose_name = "Publicação"
    verbose_name_plural = "Publicações"
    can_delete = False

    def get_fieldsets(self, request: HttpRequest, obj=...):
        fields = (
            (
                None,
                {
                    "fields": (
                        "post",
                        "get_author",
                        "get_status",
                        "get_published",
                    )
                },
            ),
        )
        return fields

    model.__str__ = lambda _: ""

    def get_status(self, obj):
        if obj.post:
            return obj.post.get_status_display()

        return "-"

    get_status.short_description = "Status"

    def get_title(self, obj):
        if obj.post:
            return obj.post.title

        return "-"

    get_title.short_description = "Título"

    def get_author(self, obj):
        if obj.post:
            return obj.post.author

        return "-"

    get_author.short_description = "Autor"

    def get_published(self, obj):
        default = " - "
        if obj.post:
            post: Post = obj.post
            return post.publish_date or default

        return default

    get_published.short_description = "Data de publicação"

    def has_add_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

    def get_field_queryset(self, db: None, db_field, request: HttpRequest):
        return super().get_field_queryset(db, db_field, request)


class CategoryAdmin(OrderedModelAdmin):
    model = Category
    list_display = [
        "__str__",
        "get_publish_number",
        "get_awaiting_for_published_number",
        "get_writing_number",
        "active",
        "move_up_down_links",
    ]
    inlines = [PostsInline]
    ordering = [
        "order",
    ]

    def get_publish_number(self, obj: Category):
        return obj.posts.filter(status=Post.PUBLISHED).count()

    get_publish_number.short_description = "Número de publicações"

    def get_awaiting_for_published_number(self, obj: Category):
        return obj.posts.filter(status=Post.AWAITING_FOR_PUBLISH).count()

    get_awaiting_for_published_number.short_description = "A publicar"

    def get_writing_number(self, obj: Category):
        return obj.posts.filter(status=Post.WRITING).count()

    get_writing_number.short_description = "Escrevendo"


class ReviewsInlineAdmin(admin.StackedInline):
    model = Reviews
    extra = 0
    readonly_fields = ["review_by", "review_date"]

    fieldsets = (
        (
            None,
            {"fields": ("title", ("review_by", "review_date"), "comment")},
        ),
    )

    def has_change_permission(self, request: HttpRequest, obj=...) -> bool:
        return False


@admin.action(description="Publicar")
def make_published(modeladmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(status=Post.PUBLISHED, publish_date=timezone.now())


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    model = Post
    actions = [make_published]
    inlines = [ReviewsInlineAdmin]
    form = PostForm
    list_display = (
        "title",
        "status",
        "slug",
        "publish_date",
        "get_published",
        "author",
    )
    list_filter = (
        "status",
        "publish_date",
    )
    list_editable = ("slug",)
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "content",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    # date_hierarchy = "publish_date"
    save_on_top = True
    list_per_page = 50
    readonly_fields = [
        "get_published",
        "status",
        "publish_date",
        "author",
    ]
    filter_horizontal = ["categories"]

    def get_fieldsets(self, request, obj=...):
        fields = (
            (
                None,
                {
                    "fields": (
                        "status",
                        "title",
                        "slug",
                        "subtitle",
                        "categories",
                    )
                },
            ),
            ("Conteúdo", {"fields": ("content", "document", "image")}),
            (
                "Publicação",
                {
                    "classes": ("collapse",),
                    "fields": (
                        "get_published",
                        "publish_date",
                        "author",
                    ),
                },
            ),
        )
        return fields

    @admin.display(boolean=True)
    def get_published(self, obj: Post):
        return obj.status == Post.PUBLISHED

    get_published.short_description = "Publicado"

    def save_formset(
        self, request: HttpRequest, form, formset, change
    ) -> None:
        objs = formset.save()
        if formset.model == Reviews:
            for obj in objs:
                obj.review_by = request.user
                obj.save()

    def save_model(self, request: HttpRequest, obj: Post, form, change):
        if obj.author is None:
            obj.author = request.user
            obj.status = Post.WRITING

        obj.save()

    def has_delete_permission(
        self, request: HttpRequest, obj: Post = None
    ) -> bool:
        if obj:
            return request.user == obj.author

        return request.user.is_superuser

    def has_change_permission(
        self, request: HttpRequest, obj: Post = None
    ) -> bool:
        if obj:
            return request.user == obj.author

        return request.user.is_superuser


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


class Site(admin.AdminSite):
    ...


# admin.site.register()
