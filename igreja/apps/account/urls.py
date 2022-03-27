from django.urls import include, path

app_name = "account"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", include("django_registration.backends.activation.urls")),
]
