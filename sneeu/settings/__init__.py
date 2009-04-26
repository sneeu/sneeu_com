# Django settings for __project__.
import logging
import os

# Get the running environment
DEBUG = False

# Set paths
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

ADMINS = MANAGERS = (
    ('Your Name', 'you@example.com',),
)

ROOT_URLCONF = 'urls'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

# Database settings
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'project.db'


CACHE_BACKEND = 'locmem:///'


SITE_ID = 1

# Email settings
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'robot@example.com'

# i18n settings
USE_I18N = True
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a secret that is a secret goes here'

# Django apps
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',

    'typogrify',

    'apps.core',
    'apps.blog',
    'apps.tumble',
    'apps.ebooks',
)


# Middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.csrf.middleware.CsrfMiddleware',
)


# Template settings
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.request',
    'apps.core.context_processors.media_url',
    'apps.core.context_processors.current_site',
)
