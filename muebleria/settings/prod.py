# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['MUEBLERIALLAVE']

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'storages',
)

# ################- CACHE ################
# PARA NO PEGARLE TAN DURO A LA b.d.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# ################- CACHE ################-

# ################- DATABASE ################
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['MUEBLERIANAME'],
        'USER': os.environ['MUEBLERIAUSER'],
        'PASSWORD': os.environ['MUEBLERIAPASSWORD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {
            'DB': 1,
            #  'PASSWORD': '',
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    }
}

THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_FORCE_OVERWRITE = True
THUMBNAIL_DEBUG = True

# ################- DATABASE ################
# ########### STATIC & MEDIA FIELDS ###########
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_FINDERS = (
    # BUSCA LOS ARCHIVOS ESTATICOS EN EL SISTEMA DE ARCHIVOS
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # BUSCA LOS ARCHIVOS ESTATICOS EN LA CARPETAS DE LAS APLICACIONES
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION _DEBUG_=_False_
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
# PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION
# STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])


MEDIA_URL = '/media/'
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ########### STATIC & MEDIA FIELDS ###########
# ########### AWS S3 SETTINGS ###########
# ######- CKEDITOR ######-
AWS_QUERYSTRING_AUTH = False
CKEDITOR_UPLOAD_PATH = "uploads_by_ckeditor/"
# ######- CKEDITOR ######-
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = 'muebleria'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# ########### AWS S3 SETTINGS ###########

# Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
# CSRF_COOKIE_SECURE = True

# Set this to True to avoid transmitting the session cookie over HTTP accidentally.
# SESSION_COOKIE_SECURE = True

