"""
Django settings for MiProyecto project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load data env
ENV = dotenv.dotenv_values()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV['DEBUG']
if DEBUG:
    try:
        DEBUG = bool(DEBUG)
    except:
        DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dbbackup',
    'productos',
    'users',
    'catalogo',
    'pqr'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MiProyecto.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'MiProyecto/plantillas'),
            os.path.join(BASE_DIR, 'productos/producto')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MiProyecto.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': ENV['DB_ENGINE'],
        'NAME': ENV['DB_NAME'],
        'USER': ENV['DB_USER'],
        'PASSWORD': ENV['DB_PASSWORD'],
        'HOST': ENV['DB_HOST'],
        'PORT': ENV['DB_PORT'],
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

# Backup
# ispath = os.path.join(BASE_DIR, 'backups')
# print(ispath)
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': './backups'}
DBBACKUP_CONNECTORS = {
    'default': {
        'DUMP_SUFFIX': '--column-statistics=0'
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'MiProyecto/static')]

MEDIA_ROOT= os.path.join(BASE_DIR,'')
MEDIA_URL ='/imagenes/'

LOGIN_REDIRECT_URL ='inicio'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field




EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST= 'smtp.gmail.com'

EMAIL_USE_TLS= True

EMAIL_PORT=587

EMAIL_HOST_USER= 'gelmarelectrodomesticos@gmail.com'

EMAIL_HOST_PASSWORD= 'ocedxcetahhciztr'


