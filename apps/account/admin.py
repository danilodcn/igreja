from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpRequest

from apps.account.models import Address, CustomUser, Profile


class AddressAdmin(admin.ModelAdmin):
    list_filter = ["id"]
    search_fields = ["id"]

    def has_view_permission(self, request: HttpRequest, obj=None):
        return True


class ProfileAdminInline(admin.StackedInline):
    model = Profile
    autocomplete_fields = ["address"]


class UserAdmin(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    list_display = ["__str__", "email", "is_active", "last_login"]
    list_filter = [
        "groups",
    ]
    inlines = [ProfileAdminInline]
    filter_horizontal = ["groups", "user_permissions"]


admin.site.register(Address, AddressAdmin)
admin.site.register(CustomUser, UserAdmin)
