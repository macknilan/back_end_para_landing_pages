# ARCHIVO PARA PODER SUBIR LOS ARCHIVOS ESTATICOS Y MEDIA 
# A AMAZON AWS S3 POR MEDIO DE ESTOS DOS PROGRAMAS django-storages Y boto
# ESTO ECHO CON DJANGO


from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION

