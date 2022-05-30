from django.urls import reverse


def get_filename(filename: str) -> str:
    return filename.lower()


def get_admin_url(obj):
    return reverse(
        "admin:%s_%s_change" % (obj._meta.app_label, obj._meta.model_name),
        args=[obj.id],
    )


def get_field_display(choices: list, value, raise_exeception=False):
    for i, choice in choices:
        if i == value:
            return choice

    if raise_exeception:
        raise ValueError(f"'{value}' não encontrado em {choices}")
