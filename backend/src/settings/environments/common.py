"""Common settings"""

from src.settings.base import env
from src.settings.components.paths import TEMPLATES_DIR

SITE_DOMAIN = env("SITE_DOMAIN", default="*")

ADMIN_USERNAME = env("ADMIN_USERNAME", default=None)
ADMIN_PASSWORD = env("ADMIN_PASSWORD", default=None)
ADMIN_EMAIL = env("ADMIN_EMAIL", default=None)

DEFAULT_FIXTURES = env.list("DEFAULT_FIXTURES", default=[])

DEBUG = env("DEBUG", default=True)

DEFAULT_DB_CONNECTION = "DATABASE_URL"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            TEMPLATES_DIR,
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                # "constance.context_processors.config",
            ],
        },
    },
]

ROOT_URLCONF = "src.urls"
WSGI_APPLICATION = "src.wsgi.application"
SITE_ID = 1
