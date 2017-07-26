from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Allow our e-mail configuration to fail if not in production
# A failure will setup Django's own e-mail backend as the default one

EMAIL_HOST = configure_variable('EMAIL_HOST', True) or 'localhost'
EMAIL_PORT = configure_variable('EMAIL_PORT', True) or 1025
EMAIL_HOST_USER = configure_variable('EMAIL_HOST_USER', True)
EMAIL_HOST_PASSWORD = configure_variable('EMAIL_HOST_PASSWORD', True)

if EMAIL_HOST_USER is None:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
