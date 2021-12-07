"""
Django settings for pjt_final_drf project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # local apps
    'accounts',
    'movies',

    # 3rd party apps
    'rest_framework', # def
    'corsheaders', # cors
    'imagekit', # imagekit
                
    # native apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # swagger
    'drf_yasg',
    'django.contrib.sites',
]

MIDDLEWARE = [
    # django cors middleware setting
    'corsheaders.middleware.CorsMiddleware',
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pjt_final_drf.urls'

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

WSGI_APPLICATION = 'pjt_final_drf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Movie-Curators',
        'USER': 'postgres',
        'PASSWORD': 'admin1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

# USE_TZ = True # naive 타임 오류 관련 수정
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


######################## image media ########################
MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'
#############################################################

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'


###########################################################################
CORS_ORIGIN_ALLOW_ALL = True
# 이후에 CORS_ORIGIN_WHITELIST 사용해서 우리가 배포하는 사이트로만 바꿔보자.

# 특정 Origin만 선택적으로 허용
# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000"
# ]

###########################################################################

'''
방문객을 최대한 늘리고 받아들이고 싶은 이번 프로젝트에서는 사용하지 않음, 프론트 차원에서 3단계에 걸친 기능 접근을 제한하는 방식으로 구현

REST_FRAMEWORK = {
    # 전역에 is_authenticated를 붙인 것과 같은 효과임
    # DRF에서 앞으로 아래에 있는 인증방식을 사용하겠다!! => 하지만 signup에서는 사용하면 안됨 => 왜? 회원가입할때 인증요청을 보낸 수 없음
    'DEFAULT_PERMISSION_CLASSES': ( # 인증되지 않은 사용자는 reject(전역)
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': ( # 토큰 자체만 보겠음! => 데코레이터로도 작성가능(이렇게 하면 전역아님) => settings.py에 쓰면 전역임
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}
'''


CSRF_COOKIE_NAME = "XSRF-TOKEN"

import datetime
JWT_AUTH = {
  'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}

SITE_ID = 1
