from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

SECRET_KEY = config('secret_key')

DEBUG = False

ALLOWED_HOSTS = ['*']

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}

sentry_sdk.init(
    dsn="https://054c4436ebfb4c93baf27c094ea43201@o4504820908818432.ingest.sentry.io/4505477586026496",
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,

    send_default_pii=True
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"