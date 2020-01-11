from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "proj1isgreat.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import proj1isgreat.users.signals  # noqa F401
        except ImportError:
            pass
