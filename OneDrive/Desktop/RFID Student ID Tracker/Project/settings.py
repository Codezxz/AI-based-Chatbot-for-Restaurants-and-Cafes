import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '$g=z2^c-js@*sscipnio6dcp@fw=v=)84^4d-6e8vpc1c(gk(='
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '$g=z2^c-js@*sscipnio6dcp@fw=v=)84^4d-6e8vpc1c(gk(=')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'login',
    'att_app',
    'django.contrib.auth',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Project.urls'
AUTH_USER_MODEL = 'login.UserModel'
AUTHENTICATION_BACKENDS = ('login.backends.MyAuthBackend','django.contrib.auth.backends.ModelBackend',)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'att_app/templates')],
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
LOGIN_REDIRECT_URL = 'login'
WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# MySQL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'rohan.deshpande@gmail.com'
SERVER_EMAIL = 'rohan.deshpande@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'rohan.deshpande@gmail.com'
EMAIL_HOST_PASSWORD = 'RNYP_1234'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

FCM_SERVER_API="AAAA0XOnFJ0:APA91bFVoUiiwpaMU12Bc0nmhSuIM1gogbTeBTD4mJwKIC5PP7tILR41wQNIGhEKp1k6R5cowDhoNBerHKJd6kCruqYsmnlgUIzdNllgc2Z5ttrgtjdsDFU9_wpn0gZj2Vhgo3X9xbxS"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'att_app/static/')
STATIC_URL = '/static/'



import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Simplified static file serving.

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
