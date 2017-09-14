from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': configure_variable('POSTGRES_DB_NAME'),
        'USER': configure_variable('POSTGRES_DB_USER'),
        'PASSWORD': configure_variable('POSTGRES_DB_PASSWORD'),
        'HOST': configure_variable('POSTGRES_DB_HOST', True, 'localhost'),
        'PORT': configure_variable('POSTGRES_DB_PORT', True, ''),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

EMAIL_BACKEND = 'sgbackend.SendGridBackend'
SENDGRID_API_KEY = configure_variable('SENDGRID_API_KEY', True, '')

# Configuring STATIC & MEDIA files storage

INSTALLED_APPS += [
    'storages',
]

AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_ACCESS_KEY_ID = configure_variable('AWS_S3_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = configure_variable('AWS_S3_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = configure_variable('AWS_STORAGE_BUCKET_NAME')

AWS_REGION = configure_variable('AWS_REGION')
AWS_S3_ENDPOINT_URL = 'https://{}.digitaloceanspaces.com'.format(AWS_REGION)

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
