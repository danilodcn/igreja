from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest

from igreja.apps.account.models import (
    Address,
    ContactMeans,
    CustomUser,
    Profile,
)
from igreja.apps.church.admin import MemberAminInline


class ContactMeansInlineAdmin(admin.TabularInline):
    search_fields = ["type", "contact"]
    model = ContactMeans
    extra = 0


class AddressAdmin(admin.ModelAdmin):
    list_filter = ["state", "address_type"]
    search_fields = ["city", "state", "zipcode", "country"]
    list_per_page = 50


class ProfileAdminInline(admin.StackedInline):
    model = Profile
    autocomplete_fields = ["address"]


class UserAdmin(UserAdmin):
    list_display = ["__str__", "email", "is_active", "last_login"]
    list_display_links = ["__str__", "email"]
    list_filter = [
        "groups",
    ]
    inlines = [ProfileAdminInline, MemberAminInline, ContactMeansInlineAdmin]
    filter_horizontal = ["groups", "user_permissions"]
    search_fields = ["first_name", "last_name"]


admin.site.register(Address, AddressAdmin)
admin.site.register(CustomUser, UserAdmin)
