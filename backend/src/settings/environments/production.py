"""Production settings"""

from src.settings.base import PRODUCTION_APPS, PRODUCTION_MIDDLEWARE, env
from src.settings.components.paths import (
    DEV_DATABASE_FILE,
    TEST_DATABASE_FILE,
)

from .common import DEFAULT_DB_CONNECTION

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

ALLOWED_HOSTS = [
    env("SITE_DOMAIN"),
]

INSTALLED_APPS = [
    *PRODUCTION_APPS,
]

MIDDLEWARE = [
    *PRODUCTION_MIDDLEWARE,
]


DATABASES = {
    "default": env.db(DEFAULT_DB_CONNECTION),
}
