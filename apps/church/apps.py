from django.apps import AppConfig


class ChurchConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.church"
    verbose_name = "Igreja"
    verbose_name_plural = "Igrejas"
