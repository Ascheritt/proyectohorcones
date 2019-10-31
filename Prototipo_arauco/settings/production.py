from .base import *
import os
import dj_database_url
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['*']
#
#    DATABASES = {
 #       'default': {
  #          'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #         'NAME': 'balanced_scorecard',
   #         'USER':  'gonza',#'gonza', postgres
   #         'PASSWORD': 'gonza30',#'gonza30',  root1234
   #         'HOST': 'localhost',
   #         'PORT': 5432,
  #      }
 #   }

 DATABASES = {
     'default': dj_database_url.config(
         default=config('DATABASE__URL')
     )
 }

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),

]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Envio de correo electronico
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'gravitron.test@gmail.com'
EMAIL_HOST_PASSWORD = 'prueba1234'
EMAIL_PORT = 587
#Tiempo de vida de la sesión en segundos
#SESSION_COOKIE_AGE = 10 

#Para que expire la sesión al cerrar el navegador. Por defecto está a False 
#SESSION_EXPIRE_AT_BROWSER_CLOSE = True 