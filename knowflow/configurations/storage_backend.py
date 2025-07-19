from django.core.files.storage import FileSystemStorage
from django.conf import settings


class MediaStorage(FileSystemStorage):
    """
    Custom media file storage class.
    Uses MEDIA_ROOT and MEDIA_URL from settings.
    """
    def __init__(self, *args, **kwargs):
        kwargs["location"] = settings.MEDIA_ROOT
        kwargs["base_url"] = settings.MEDIA_URL
        super().__init__(*args, **kwargs)