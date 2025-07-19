from enum import Enum

# File Model Constants
FILE_APP = "apps.file"

FILE_TITLE_MAX_LEN = 100
FILE_UPLOAD_PATH = "documents/"

# Error messages
INVALID_FILE_TYPE = "Unsupported file extension: {}. Allowed: PDF, DOC, DOCX, MD"


class DocumentExtension(str, Enum):
    PDF = '.pdf'
    DOC = '.doc'
    DOCX = '.docx'
    MD = '.md'
    MARKDOWN = '.markdown'

    @classmethod
    def list(cls):
        return [e.value for e in cls]