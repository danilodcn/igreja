from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from ordered_model.admin import (
    OrderedModelAdmin,
    OrderedStackedInline,
    OrderedTabularInline,
)

from .models import Category, Event, EventPaymentOption, Subscription


class CategoryAdmin(OrderedModelAdmin):
    search_fields = ["name"]


class EventPaymentOptionInline(OrderedTabularInline):
    model = EventPaymentOption
    readonly_fields = ["move_up_down_links"]
    extra = 0


class EventForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), label="Conteúdo")


class EventAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    inlines = [EventPaymentOptionInline]
    form = EventForm
    autocomplete_fields = ["address", "church", "category"]


class SubscriptionAdmin(OrderedModelAdmin):
    search_fields = ["pk"]
    autocomplete_fields = ["event", "payment", "user", "updated_by"]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
