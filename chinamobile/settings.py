# -*- coding: utf-8 -*-

"""
Django settings for agricom project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '2)_=7-&&xcje-jbinyc%&(+u53-fwpsf9+$jrv8#+vra-izmzt'
SECRET_KEY = config('SECRET_KEY', default='s3cr3t_k3y')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',default='True',cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv(), default=['127.0.0.1', 'localhost'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    #'reporter'
    'reporter.apps.ReporterConfig', # 支持在`admin`,显示`app`中文名
    'rest_framework',
    #'sslserver',
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
]

ROOT_URLCONF = 'chinamobile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'chinamobile.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'HOST': config('DB_HOST'),
        'PASSWORD': config('DB_PASSWORD'),
        'PORT': config('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'
 

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)


# 设置静态文件目录
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (37.5335,121.3920), # yantai
    #'DEFAULT_CENTER': (-.023,36.87), # nairobi
    #'SPATIAL_EXTENT': (119.5582,36.5732, 121.9295,38.4022),
    'DEFAULT_ZOOM': 8,
    'MAX_ZOOOM': 20,
    'MIN_ZOOM':3,
    #'SCALE': 'imperial'
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': '烟台麦卡托信息技术有限公司 © Maikator Co., Ltd. 2018',
    'TILES': [('开放街道地图','https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{}),
              ('Mapbox街道地图', 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {'id': 'mapbox.streets', 'maxZoom': '18','accessToken': 'pk.eyJ1Ijoiemh1Z3VhbmdqdW4yMDAyIiwiYSI6ImNqYzFkNGl2ZjAwa2oyeW4yMGh0cTAxcHAifQ.bbY8ctOlYyb77S4P0VZ25A'})],
    'OVERLAYS': [('Mapbox卫星影像', 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {'id': 'mapbox.satellite', 'maxZoom': '18','accessToken':'pk.eyJ1Ijoiemh1Z3VhbmdqdW4yMDAyIiwiYSI6ImNqYzFkNGl2ZjAwa2oyeW4yMGh0cTAxcHAifQ.bbY8ctOlYyb77S4P0VZ25A'})]
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 如果启用，则用户不需要登录，就可以读取postings.
        #　因为，可以只读，就不需要认证了。
        # 这个权限的意思是，只要认证通过，或者只读，就授权，就允许。
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # README.md 要求添加。
        # 这样，只有那些认证了的，才有权限，没有被认证的，访问都拒绝。
        # 这是最简单的权限管理方式。
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # README.md 要求添加，这样提供了基本的认证功能。
        # 'rest_framework.authentication.BasicAuthentication',
    ),
}


JWT_AUTH = {
    # 'JWT_ENCODE_HANDLER':
    # 'rest_framework_jwt.utils.jwt_encode_handler',

    # 'JWT_DECODE_HANDLER':
    # 'rest_framework_jwt.utils.jwt_decode_handler',

    # 'JWT_PAYLOAD_HANDLER':
    # 'rest_framework_jwt.utils.jwt_payload_handler',

    # 'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    # 'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    # 'JWT_RESPONSE_PAYLOAD_HANDLER':
    # 'rest_framework_jwt.utils.jwt_response_payload_handler',

    # 'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_SECRET_KEY': 'yantai2018',
    # 'JWT_GET_USER_SECRET_KEY': None,
    # 'JWT_PUBLIC_KEY': None,
    # 'JWT_PRIVATE_KEY': None,
    # 'JWT_ALGORITHM': 'HS256',
    # 'JWT_VERIFY': True,
    # 'JWT_VERIFY_EXPIRATION': True,
    # 'JWT_LEEWAY': 0,
    # 'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
    # 'JWT_AUDIENCE': None,
    # 'JWT_ISSUER': None,

    # 'JWT_ALLOW_REFRESH': False,
    'JWT_ALLOW_REFRESH': True,
    # 'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

    # 'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_HEADER_PREFIX': 'Bearer',
    # 'JWT_AUTH_COOKIE': None,
}

# Enable HTTPS SSL
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = '/'
