from os.path import join

from apps.conversation.settings import CONVERSATION_APP
from apps.file.settings import FILE_APP
from .configurations.common_settings import BASE_DIR
from .configurations.env_helpers import get_env_var, get_bool_env_var, get_list_env_var, get_int_env_var
from .configurations.logger_settings import LOGGING
from .configurations.spectacular_settings import SPECTACULAR_SETTINGS
from .configurations.rest_framework_settings import REST_FRAMEWORK
from .configurations.jwt_settings import SIMPLE_JWT
from .configurations.storage_settings import *
from .configurations.database_settings import (
    postgres_settings,    
    REDIS_HOST,
    REDIS_PORT
)

from .configurations.celery_settings import (
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND,
    CELERY_CACHE_BACKEND,
    CELERY_RESULT_EXTENDED,
    CELERY_RESULT_EXPIRES
)


""" 
Application Definition Start.
"""

ENVIRONMENT = get_env_var("ENVIRONMENT")
SECRET_KEY = get_env_var("SECRET_KEY")
DEBUG = get_bool_env_var("DEBUG")

CORE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "corsheaders",
    "import_export",
    "drf_spectacular",

    
    'django_celery_results',
    
]

PROJECT_APPS = [
    "apps.user",
    FILE_APP,
    CONVERSATION_APP,
]

INSTALLED_APPS = CORE_APPS + PROJECT_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
ALLOWED_HOSTS = get_list_env_var("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = get_list_env_var("CSRF_TRUSTED_ORIGINS")

ROOT_URLCONF = "knowflow.urls"
WSGI_APPLICATION = "knowflow.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

"""
Application Definition End.
"""

""" 
Database Settings Start.
"""

DATABASES = {
    "default": postgres_settings,
}

""" 
Database Settings End.
"""

"""
Authentication & Authorization Settings Start.
"""

AUTH_USER_MODEL = "user.User"
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_RESET_TIMEOUT = get_int_env_var("PASSWORD_RESET_TIMEOUT")

"""
Authentication & Authorization Settings End.
"""

"""
Internationalization Settings Start.
"""

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

"""
Internationalization Settings End.
"""
