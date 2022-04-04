from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class TagAdmin(admin.ModelAdmin):
    model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "slug",
        "published",
    )
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
    date_hierarchy = "publish_date"
    save_on_top = True
    readonly_fields = [
        "get_published",
        "status",
        "publish_date",
        "author",
        "reviewed_by",
        "review_date",
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
                        "reviewed_by",
                        "review_date",
                    ),
                },
            ),
        )
        return fields

    @admin.display(boolean=True)
    def get_published(self, obj):
        return obj.published

    get_published.short_description = "Publicado"
