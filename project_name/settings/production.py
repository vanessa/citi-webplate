from .base import *

DEBUG = False

'''
Check if DATABASE_URL exists in the environment so we 
can use dj_database_url to set the DB automatically. If 
not, we use our environment.py files to configure 
manually a psql database.
'''
if 'DATABASE_URL' in os.environ:
    default_db = dj_database_url.config(conn_max_age=500)
else:
    db_url = 'postgres://{}:{}@{}:{}/{}'.format(
        configure_variable('POSTGRES_DB_USER'), # USER
        configure_variable('POSTGRES_DB_PASSWORD'), #PASSWORD
        configure_variable('POSTGRES_DB_HOST', True, 'localhost'), #HOST
        configure_variable('POSTGRES_DB_PORT', True, ''), #PORT
        configure_variable('POSTGRES_DB_NAME') #NAME
    )
    default_db = dj_database_url.config(default=db_url, conn_max_age=500)

DATABASES['default'].update(default_db)

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

# Configuring STATIC files serving using whitenoise

MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuring MEDIA files storage using Amazon S3

INSTALLED_APPS += [
    'storages',
]

AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_ACCESS_KEY_ID = configure_variable('AWS_S3_ACCESS_KEY_ID', True, '')
AWS_S3_SECRET_ACCESS_KEY = configure_variable('AWS_S3_SECRET_ACCESS_KEY', True, '')
AWS_STORAGE_BUCKET_NAME = configure_variable('AWS_STORAGE_BUCKET_NAME', True, '')

AWS_REGION = configure_variable('AWS_REGION')
AWS_S3_ENDPOINT_URL = 'https://{}.digitaloceanspaces.com'.format(AWS_REGION, True, '')

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
