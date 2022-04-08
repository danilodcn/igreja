from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest

from apps.account.models import Address, CustomUser, Profile
from apps.church.admin import MemberAminInline


class AddressAdmin(admin.ModelAdmin):
    list_filter = ["state", "address_type"]
    search_fields = ["city", "state", "zipcode", "country"]
    list_per_page = 50


class ProfileAdminInline(admin.StackedInline):
    model = Profile
    autocomplete_fields = ["address"]


class UserAdmin(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    list_display = ["__str__", "email", "is_active", "last_login"]
    list_filter = [
        "groups",
    ]
    inlines = [ProfileAdminInline, MemberAminInline]
    filter_horizontal = ["groups", "user_permissions"]
    search_fields = ["first_name", "last_name"]


admin.site.register(Address, AddressAdmin)
admin.site.register(CustomUser, UserAdmin)
