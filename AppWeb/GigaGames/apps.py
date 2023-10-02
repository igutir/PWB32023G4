from django.apps import AppConfig


class GigagamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GigaGames'

    def ready(self):
        import GigaGames.signals
