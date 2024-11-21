"""
Django settings for alertwise project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from email.utils import getaddresses

import dj_database_url
import environ

from alertwise import VERSION

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
)

dev_env_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(BASE_DIR))), ".env")

if os.path.isfile(dev_env_path):
    # reading .env file
    environ.Env.read_env(dev_env_path)

# Application definition
INSTALLED_APPS = [
    "alertwise.capeditor",
    "alertwise.cap",
    "alertwise.home",
    "adminboundarymanager",
    
    "wagtailiconchooser",
    "wagtailhumanitarianicons",
    "wagtail_lazyimages",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.contrib.styleguide",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    
    "wagtail_modeladmin",
    'wagtailmodelchooser',
    "wagtailfontawesomesvg",
    
    "modelcluster",
    "taggit",
    "wagtailcache",
    "django_countries",
    "django_celery_beat",
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.gis",
    
    "django_deep_translator",
    "dbbackup",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "alertwise.config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "alertwise.config.wsgi.application"
ASGI_APPLICATION = "alertwise.config.asgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = env.str("LANGUAGE_CODE", default="en")

TIME_ZONE = env.str("TIME_ZONE", "UTC")

print(env.str("DB_NAME"), LANGUAGE_CODE)

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = env.str("STATIC_ROOT", os.path.join(BASE_DIR, "static"))
STATIC_URL = "/static/"

MEDIA_ROOT = env.str("MEDIA_ROOT", os.path.join(BASE_DIR, "media"))
MEDIA_URL = "/media/"

# Default storage settings, with the staticfiles storage updated.
# See https://docs.djangoproject.com/en/5.0/ref/settings/#std-setting-STORAGES
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    # ManifestStaticFilesStorage is recommended in production, to prevent
    # outdated JavaScript / CSS assets being served from cache
    # (e.g. after a Wagtail upgrade).
    # See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
    "staticfiles": {
        "BACKEND": "alertwise.config.storage.ManifestStaticFilesStorageNotStrict",
    },
}

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': os.path.join(BASE_DIR, "backup")}
DBBACKUP_CLEANUP_KEEP_MEDIA = 1
DBBACKUP_CLEANUP_KEEP = 1
DBBACKUP_CONNECTORS = {
    "default": {
        "CONNECTOR": "dbbackup.db.postgresql.PgDumpBinaryConnector",  # Use pg_dump binary
        "DUMP_SUFFIX": "-e plpgsql",  # dump only system extensions
        "RESTORE_SUFFIX": "--if-exists"  # Drop only if exists
    }
}

# Wagtail settings
WAGTAIL_SITE_NAME = env.str("WAGTAIL_SITE_NAME", "AlertWise")

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

# Allowed file extensions for documents in the document library.
# This can be omitted to allow all files, but note that this may present a security risk
# if untrusted users are allowed to upload files -
# see https://docs.wagtail.org/en/stable/advanced_topics/deploying.html#user-uploaded-files
WAGTAILDOCS_EXTENSIONS = ['csv', 'docx', 'key', 'odt', 'pdf', 'pptx', 'rtf', 'txt', 'xlsx', 'zip']

# Wagtail Geowidget settings
GEO_WIDGET_DEFAULT_LOCATION = {'lat': 0, 'lng': 0}
GEO_WIDGET_ZOOM = 3

REDIS_HOST = env.str("REDIS_HOST", "redis")
REDIS_PORT = env.str("REDIS_PORT", "6379")
REDIS_USERNAME = env.str("REDIS_USER", "")
REDIS_PASSWORD = env.str("REDIS_PASSWORD", "")
REDIS_PROTOCOL = env.str("REDIS_PROTOCOL", "redis")
REDIS_URL = env.str(
    "REDIS_URL",
    f"{REDIS_PROTOCOL}://{REDIS_USERNAME}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0",
)

CELERY_BROKER_URL = REDIS_URL
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CELERY_SINGLETON_BACKEND_CLASS = (
    "alertwise.config.celery_singleton_backend.RedisBackendForSingleton"
)

CELERY_APP = "alertwise.config.celery:app"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        "KEY_PREFIX": "alertwise-default-cache",
        "VERSION": VERSION,
        "TIMEOUT": 60 * 60 * 4,  # 4 hours
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        # Send logs with at least INFO level to the console.
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s][%(process)d][%(levelname)s][%(name)s] %(message)s"
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

MAX_CAP_LIST_PAGE_COUNT = env("MAX_CAP_LIST_PAGE_COUNT", default=None)

CAP_ALLOW_EDITING = env.bool("CAP_ALLOW_EDITING", default=False)

DATA_UPLOAD_MAX_MEMORY_SIZE = env.int("DATA_UPLOAD_MAX_MEMORY_SIZE", default=26214400)  # 25MB

# EMAIL SETTINGS
# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="")

# A list of people who get error notifications.
ADMINS = getaddresses([env('DJANGO_ADMINS', default="")])

# A list in the same format as ADMINS that specifies who should get some content management errors
MANAGERS = ADMINS + getaddresses([env('DJANGO_MANAGERS', default="")])

# A list in the same format as DEVELOPERS for receiving developer aimed messages
DEVELOPERS = getaddresses([env('DJANGO_APP_DEVELOPERS', default="")])

# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL
