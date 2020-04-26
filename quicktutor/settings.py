"""
Django settings for quicktutor project.
Generated by 'django-admin startproject' using Django 3.0.2.
For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
import psycopg2


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static')
)
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/images')
MEDIA_URL = '/media/'

#Used for Dotenv SQL Lite Test
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm7vq@&i*#1b83uf9_2qvt$*s2_)vm7-m87mfx%66aer33&z#fn'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '849030481645-8laklq9ameqka9a9ah39aj7mfehgbq8v'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'AMW0SNMewsnkhblijI2CG0DJ'

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/login/authflow/'
LOGOUT_REDIRECT_URL = '/login/logout/'

# SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['virginia.edu']
# SOCIAL_AUTH_LOGIN_ERROR_URL = '/login/authentication_error/'
# SOCIAL_AUTH_RAISE_EXCEPTIONS = False
# SOCIAL_AUTH_BACKEND_ERROR_URL = '/login/authentication_error/'

SOCIAL_AUTH_URL_NAMESPACE = 'login:social'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    # 'modular.pipeline.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
    'login.pipeline.save_profile'
)



ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# Application definition

INSTALLED_APPS = [
    'bootstrap_modal_forms',
    'crispy_forms',
    'home.apps.HomeConfig', # ???
    'login.apps.LoginConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'quicktutor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'quicktutor.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases





# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Activate Django-Heroku.
try:
    import django_heroku
    django_heroku.settings(locals()) # test runner option to fix travis tests
except ImportError as exc:
    pass

DATABASES = {}

# Dotenv SQL Lite Test
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# Indicates that model UserProfile is the user profile
AUTH_PROFILE_MODULE = 'login.UserProfile'

