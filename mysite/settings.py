"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.2.15.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

#AUTH_USER_MODEL = 'empresa.models.usuario'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x4$6a5zr*w7z)8i)j@ud3z_#8b%oj_ndfx3-7ja4n)_byd_&x5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', 'pythonanywhere.com', '190.131.29.88']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'rest_framework',
    'clienteWA.apps.ClientewaConfig',
    'corsheaders',
    'empresa.apps.EmpresaConfig',
    'channels',
    'chat',
    'notificaciones'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #Se comentó esta linea porque daba error de peticiones csrf
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Next, set CORS_ORIGIN_ALLOW_ALL and add the host to CORS_ORIGIN_WHITELIST:

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://121.0.0.1:8000',
    'ws://localhost:8000',

    'wss://seproamerica2022.pythonanywhere.com',
    'https://seproamerica2022.pythonanywhere.com'

)



ROOT_URLCONF = 'mysite.urls'

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
            ],
        },
    },
]

ASGI_APPLICATION = 'mysite.asgi.application'
WSGI_APPLICATION = 'mysite.wsgi.application'


CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

'''CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}'''


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seproamerica2022$seproamericadb',
        'USER': 'seproamerica2022',
        'PASSWORD': 'Admin2022',
        'HOST': 'seproamerica2022.mysql.pythonanywhere-services.com'
        #'PORT': '3306',


    }
}

'''
desarrollo
        'NAME': 'seproamericadb',
        'USER': 'root',
        'PASSWORD': 'Admin',
        'HOST': 'localhost',
        'PORT': '3306',

'NAME': 'seproamerica11',
        'USER': 'root',
        'PASSWORD': 'centro234',
        'HOST': 'localhost',
        'PORT': '3306'
  
'''
'''
produccion
        'NAME': 'seproamerica2022$seproamericadb',
        'USER': 'seproamerica2022',
        'PASSWORD': 'Admin2022',
        'HOST': 'seproamerica2022.mysql.pythonanywhere-services.com'
        #'PORT': '3306',

'''

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
#STATICFILES_DIRS = [
#    BASE_DIR + "/static"
#]
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')




# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
