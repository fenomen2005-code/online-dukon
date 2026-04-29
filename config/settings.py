
import os
from pathlib import Path

from environs import Env

os.makedirs('templates', exist_ok=True)

env = Env()
env.read_env()
BASE_DIR=Path(__file__).resolve().parent.parent

SECRET_KEY=env.str('SECRET_KEY')
DEBUG=env.bool('DEBUG')
ALLOWED_HOSTS=env.list('ALLOWED_HOSTS')

LOGIN_URL = '/login/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'shop',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
       
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             BASE_DIR / 'templates'
             ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
   DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'DB_NAME': env.str('DB_NAME'),
            'DB_USER': env.str('DB_USER'),
            'DB_PASSWORD': env.str('DB_PASSWORD'),
            'DB_HOST': env.str('DB_HOST'),
            'DB_PORT': env.int('DB_PORT'),
    }
}
    





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



LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


os.makedirs('templates', exist_ok=True)
os.makedirs('staticfiles', exist_ok=True)
os.makedirs('static', exist_ok=True)
os.makedirs('media', exist_ok=True)

# ishlab chiqarish jarayonidagi staitik kerakli faqyllar
STATICFILES_DIRS = [BASE_DIR / 'staticfiles',
]
# serverga quyganimzda admin paneli stillari qayerda ekanligini korsatib turadi
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
# ?foydalanuvchi resurslari saqlanadigan joy
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULD_AUTO_FIELD = 'django.db.models.BigAutoField'