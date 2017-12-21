from .base import *

DEBUG = True

db_url = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'test.sqlite3'))
default_db = dj_database_url.config(default=db_url, conn_max_age=None)
DATABASES['default'].update(default_db)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
