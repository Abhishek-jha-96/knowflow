
from .env_helpers import get_env_var, get_int_env_var

POSTGRES_DB = get_env_var("POSTGRES_DB")
POSTGRES_USER = get_env_var("POSTGRES_USER")
POSTGRES_PASSWORD = get_env_var("POSTGRES_PASSWORD")
POSTGRES_HOST = get_env_var("POSTGRES_HOST")
POSTGRES_PORT = get_int_env_var("POSTGRES_PORT")

postgres_settings = {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": POSTGRES_DB,
    "USER": POSTGRES_USER,
    "PASSWORD": POSTGRES_PASSWORD,
    "HOST": POSTGRES_HOST,
    "PORT": POSTGRES_PORT
}





MONGO_HOST = get_env_var("MONGO_HOST")
MONGO_PORT = get_env_var("MONGO_PORT")
MONGO_INITDB_ROOT_USERNAME = get_env_var("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = get_env_var("MONGO_INITDB_ROOT_PASSWORD")
MONGO_INITDB_DATABASE = get_env_var("MONGO_INITDB_DATABASE")
MONGO_INITDB_USERNAME = get_env_var("MONGO_INITDB_USERNAME")
MONGO_INITDB_PASSWORD = get_env_var("MONGO_INITDB_PASSWORD")

host_string = (
    'mongodb://'
    f'{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@'
    f'{MONGO_PORT}:{MONGO_PORT}/'
)

mongodb_settings = {
    "ENGINE": "djongo",
    "ENFORCE_SCHEMA": False,
    "NAME": MONGO_INITDB_DATABASE,
    "CLIENT": {
        'host': host_string,
        'username': MONGO_INITDB_USERNAME,
        'password': MONGO_INITDB_PASSWORD
    }
}





REDIS_HOST = get_env_var("REDIS_HOST")
REDIS_PORT = get_int_env_var("REDIS_PORT")


