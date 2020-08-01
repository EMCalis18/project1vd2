from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado', 
        'USER': 'elian', 
        'PASSWORD': 'riverplate18',
        'HOST': 'localhost', 
        'PORT': '5432', 

    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')] #DIR = DIRECTORIO DE LOS ARCHIVOS STATIC

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')