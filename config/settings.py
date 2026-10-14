
from pathlib import Path
import os

from dotenv import load_dotenv


# ============================================================
# 1. CHEMIN PRINCIPAL DU PROJET
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Charger les variables d'environnement
load_dotenv(BASE_DIR / ".env")


# ============================================================
# 2. SÉCURITÉ DJANGO
# ============================================================

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

if not SECRET_KEY:
    raise RuntimeError(
        "DJANGO_SECRET_KEY est manquante. "
        "Configurez cette variable dans le fichier .env."
    )

DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get(
        "DJANGO_ALLOWED_HOSTS",
        "127.0.0.1,localhost"
    ).split(",")
    if host.strip()
]


# ============================================================
# 3. APPLICATIONS INSTALLÉES
# ============================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Application du portfolio
    "portfolio",
]


# ============================================================
# 4. MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ============================================================
# 5. URL ET WSGI
# ============================================================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# ============================================================
# 6. CONFIGURATION DES TEMPLATES
# ============================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
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


# ============================================================
# 7. BASE DE DONNÉES SQLITE
# ============================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ============================================================
# 8. VALIDATION DES MOTS DE PASSE
# ============================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# ============================================================
# 9. LANGUE ET FUSEAU HORAIRE
# ============================================================

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_TZ = True


# ============================================================
# 10. FICHIERS STATIQUES : CSS, JS, IMAGES
# ============================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"


# ============================================================
# 11. CLÉ PRIMAIRE PAR DÉFAUT
# ============================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ============================================================
# 12. PARAMÈTRES DE SÉCURITÉ
# ============================================================

SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = "DENY"

# Ces protections HTTPS seront activées en production.
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
