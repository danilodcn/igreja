from django import forms
from django.contrib import admin

from .models import Church, Member, MemberType


class MemberAminInline(admin.TabularInline):
    extra = 0
    model = Member
    autocomplete_fields = ["member", "member_type", "church"]

    model.__str__ = lambda _: ""


class MembrerTypeAdmin(admin.ModelAdmin):
    inlines = [MemberAminInline]

    search_fields = ["name", "code"]


class ChurchAdminForm(forms.ModelForm):
    class Meta:
        model = Church
        exclude = ["members"]


class ChurchAdmin(admin.ModelAdmin):
    form = ChurchAdminForm
    list_display = [
        "__str__",
        "is_default",
        "get_membres_number",
        "active",
    ]
    autocomplete_fields = ["address"]
    search_fields = ["code", "name"]
    list_per_page = 25

    list_filter = [
        ("address__state", admin.AllValuesFieldListFilter),
    ]

    inlines = [
        MemberAminInline,
    ]

    @admin.display(description="Número de membros")
    def get_membres_number(self, obj: Church):
        return obj.members.all().count()


admin.site.register(MemberType, MembrerTypeAdmin)
admin.site.register(Church, ChurchAdmin)
