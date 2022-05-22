from django.db.models import Count
from django_admin_multiple_choice_list_filter.list_filters import (
    MultipleChoiceListFilter,
)


class ChurchFilter(MultipleChoiceListFilter):
    title = "Church"
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
