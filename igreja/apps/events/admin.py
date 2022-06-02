from django.contrib import admin
from ordered_model.admin import (
    OrderedModelAdmin,
    OrderedStackedInline,
    OrderedTabularInline,
)

from .models import Category, Event, EventPaymentOption, Subscription


class CategoryAdmin(OrderedModelAdmin):
    ...


class EventPaymentOptionInline(OrderedStackedInline):
    model = EventPaymentOption


class EventAdmin(admin.ModelAdmin):
    inlines = [EventPaymentOptionInline]


class SubscriptionAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
