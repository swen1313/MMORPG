from django.apps import AppConfig


class MmorpgappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mmorpgapp'
    def ready(self):
        import mmorpgapp.signals
