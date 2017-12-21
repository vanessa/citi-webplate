from .base import *

DEBUG = True

db_url = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
default_db = dj_database_url.config(default=db_url, conn_max_age=500)
DATABASES['default'].update(default_db)

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '',
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
