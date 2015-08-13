# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['MUEBLERIALLAVE']

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'storages',
)

# --------------------------------- CACHE ---------------------------------
# PARA NO PEGARLE TAN DURO A LA b.d.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# --------------------------------- CACHE ---------------------------------

# --------------------------------- DATABASE ---------------------------------
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'NAME',
        'USER': 'USER',
        'PASSWORD': 'PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# --------------------------------- DATABASE ---------------------------------

# ---------------------- STATIC & MEDIA FIELDS ----------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'muebleria/static'),
)

# PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION _DEBUG_=_False_
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
# PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])

STATICFILES_FINDERS = (
    # BUSCA LOS ARCHIVOS ESTATICOS EN EL SISTEMA DE ARCHIVOS
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # BUSCA LOS ARCHIVOS ESTATICOS EN LA CARPETAS DE LAS APLICACIONES
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'muebleria/media')
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])

# ---------------------- STATIC & MEDIA FIELDS ----------------------
# ---------------------- AWS S3 SETTINGS ----------------------
AWS_STORAGE_BUCKET_NAME = 'muebleria'
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# ---------------------- AWS S3 SETTINGS ----------------------


# Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
# CSRF_COOKIE_SECURE = True

# Set this to True to avoid transmitting the session cookie over HTTP accidentally.
# SESSION_COOKIE_SECURE = True





