from django.apps import AppConfig

from apps.file.settings import FILE_APP


class FileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = FILE_APP

    def ready(self):
        import apps.file.signals