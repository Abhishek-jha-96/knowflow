import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

# Static files (CSS, JavaScript, etc.)
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"  # where `collectstatic` stores files

# Media files (uploaded by users)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Storages config
STORAGES = {
    "default": {
        "BACKEND": "knowflow.configurations.storage_backend.MediaStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
