from django.db import models
from apps.core.models import Timestamps
from apps.file.settings import FILE_TITLE_MAX_LEN, FILE_UPLOAD_PATH
from apps.file.utils import validate_file_extension
from knowflow.configurations.storage_backend import MediaStorage


class File(Timestamps):
    title = models.CharField(max_length=FILE_TITLE_MAX_LEN)
    file = models.FileField(
        upload_to=FILE_UPLOAD_PATH,
        storage=MediaStorage(),
        validators=[validate_file_extension]
    )

    def __str__(self):
        return self.title
