from apps.account.forms import CustomUserForm
from django.urls import include, path
from django_registration.backends.activation.views import RegistrationView

app_name = "account"

urlpatterns = [
    path(
        "register/",
        RegistrationView.as_view(form_class=CustomUserForm),
        name="registration",
    ),
    path(
        "",
        include("django_registration.backends.activation.urls"),
    ),
    path("", include("django.contrib.auth.urls")),
]
