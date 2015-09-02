# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['MUEBLERIALLAVE']

INSTALLED_APPS += (
    'django_extensions',
    'storages',
)

DEBUG = True

ALLOWED_HOSTS = []

# --------------------------------- DATABASE ---------------------------------
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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# --------------------------------- DATABASE ---------------------------------

# ---------------------- STATIC & MEDIA FIELDS ----------------------
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION DEBUG = False
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'
# PARA PONER CACHE LOS ARCHIVOS ESTATICOS EN PRODUCCION
STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['content'])

STATICFILES_FINDERS = (
    # BUSCA LOS ARCHIVOS ESTATICOS EN EL SISTEMA DE ARCHIVOS
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # BUSCA LOS ARCHIVOS ESTATICOS EN LA CARPETAS DE LAS APLICACIONES
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['media'])

# ------------- CKEDITOR -------------
AWS_QUERYSTRING_AUTH = False
CKEDITOR_UPLOAD_PATH = "uploads_by_ckeditor/"
# ------------- CKEDITOR -------------
# ---------------------- STATIC & MEDIA FIELDS ----------------------
# ----------------------SEND EMAILS----------------------
EMAIL_USE_TLS = True
"""EMAIL_HOST = 'EMAIL_HOST'"""
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
"""EMAIL_HOST_USER = 'EMAIL_HOST_USER'"""
EMAIL_HOST_USER = 'nomackayu@gmail.com'
"""EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'"""
EMAIL_HOST_PASSWORD = 'EMAIL_HOST_PASSWORD'
# ----------------------SEND EMAILS----------------------
# ---------------------------------- django-ckeditor ----------------------------------
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'UltraFull',
        'height': 300,
        'toolbar_UltraFull': [
            ['Source', '-', 'Save', 'NewPage', 'DocProps', 'Preview', 'Print', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Find', 'Replace', '-', 'SelectAll', '-', 'SpellChecker', 'Scayt'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About'],
        ],
        'forcePasteAsPlainText': True,
    },
}
# ---------------------------------- django-ckeditor ----------------------------------





























