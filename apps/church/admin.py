from django.contrib import admin

from .models import Church, MembrerType


@admin.register(MembrerType)
class MembrerTypeAdmin(admin.ModelAdmin):
    ...
