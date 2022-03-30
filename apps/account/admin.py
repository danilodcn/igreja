from django.contrib import admin
from apps.account.models import Address, CustomUser, Profile


class AddressAdmin(admin.ModelAdmin):
    list_filter = ["id"]
    search_fields = ["id"]

    def has_view_permission(self, request, obj=None):
        return True


class ProfileAdminInline(admin.StackedInline):
    model = Profile
    autocomplete_fields = ["address"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "__str__"]
    list_filter = ["is_superuser", "is_staff"]

    inlines = [ProfileAdminInline]


admin.site.register(Address, AddressAdmin)
admin.site.register(CustomUser, UserAdmin)
