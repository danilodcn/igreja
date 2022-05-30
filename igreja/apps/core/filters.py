from django.db.models import Count
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)

from .utils import get_field_display


class ChurchFilter(MultipleChoiceListFilter):
    title = "Igreja"
    parameter_name = "church_id__in"

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)

        for pk, name, count in (
            qs.values_list("church__id", "church__name")
            .annotate(total=Count("church_id"))
            .order_by("-total")
        ):
            if count:
                yield (pk, f"{name} ({count})")


class TypePageConfigFilter(MultipleChoiceListFilter):
    title = "Tipo de Página"
    parameter_name = "type__in"

    def lookups(self, request, model_admin):
        PAGE_TYPES = model_admin.model.PAGE_TYPES
        qs = model_admin.get_queryset(request)
        for pk, type, count in (
            qs.values_list("pk", "type")
            .annotate(total=Count("type"))
            .order_by("-total")
        ):
            if count:
                name = get_field_display(PAGE_TYPES, type)
                yield (pk, f"{name} ({count})")
