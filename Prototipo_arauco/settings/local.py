from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'balance_scorecard/templates'), ],
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

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'balanced_scorecard',
        'USER':  'gonza',#'gonza', postgres
        'PASSWORD': 'gonza30',#'gonza30',  root1234
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

STATICFILES_FINDERS = [
    # searches in STATICFILES_DIRS
    'django.contrib.staticfiles.finders.FileSystemFinder',
    # searches in STATIC subfolder of each app
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

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