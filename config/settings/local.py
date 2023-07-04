from .base import *

SECRET_KEY = 'adrian$%6"#WQEfs546756uyer45656u7gEDFG'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}