from django.urls import include, path

app_name = "account"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]
