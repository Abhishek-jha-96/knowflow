import os
import re

from django.core.exceptions import ValidationError

from apps.file.settings import INVALID_FILE_TYPE, DocumentExtension

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in DocumentExtension.list():
        raise ValidationError(INVALID_FILE_TYPE.format(ext))


def sanitize_collection_name(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', name)