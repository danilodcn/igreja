from apps.account.models import CustomUser
from django_registration.forms import RegistrationForm


class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser

    def as_p(self):
        import ipdb

        ipdb.set_trace()
        return super().as_p()
