import time
import django.db.models.signals
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from config.environment import BASE_DIR, settings

# Sentry Configuration
# https://docs.sentry.io/platforms/python/integrations/django/

sentry_sdk.init(
    dsn=settings.SENTRY_DSN,
    send_default_pii=True,
    integrations=[
        DjangoIntegration(
            transaction_style="url",
            middleware_spans=True,
            signals_spans=True,
            signals_denylist=[
                django.db.models.signals.pre_init,
                django.db.models.signals.post_init,
            ],
            cache_spans=False,
            http_methods_to_capture=("GET",),
        ),
    ],
)

# General Settings

APP_ENV = settings.APP_ENV

SECRET_KEY = settings.SECRET_KEY

DEBUG = settings.DEBUG

SECURE_REFERRER_POLICY = "no-referrer-when-downgrade"

SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin-allow-popups"

ALLOWED_HOSTS = settings.get_allowed_hosts()

CSRF_TRUSTED_ORIGINS = settings.get_trusted_origins()

CORS_ALLOWED_ORIGINS = settings.get_trusted_origins()

if settings.APP_ENV == "development":
    CORS_ALLOW_ALL_ORIGINS = True


# Application definition

THIRD_PARTY_APPS = [
    "corsheaders",
    "django_tailwind_cli",
]

LOCAL_APPS = [
    "app.home",
    "app.speakers",
    "app.sponsors",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

if settings.APP_ENV == "development":
    INSTALLED_APPS.insert(0, "whitenoise.runserver_nostatic")


LOCAL_MIDDLEWARE = [
    "config.middleware.HealthCheckMiddleware",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    *LOCAL_MIDDLEWARE,
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

if settings.APP_ENV == "development":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "DISABLE_SERVER_SIDE_CURSORS": True,
            **settings.get_db_config(),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "mediafiles"
MEDIA_URL = "/media/"

# Django Tailwind CLI
# https://django-tailwind-cli.readthedocs.io/latest/

TAILWIND_CLI_SRC_CSS = "src/styles/main.css"
TAILWIND_CLI_DIST_CSS = "css/app.css"

TAILWIND_CLI_USE_DAISY_UI = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
