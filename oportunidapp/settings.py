import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "ia=1dinj8#(uo!_hdzf6jh3_==w99!3r98m=6$8z=7n7%%h79^"

DEBUG = True

TEMPLATE_DEBUG = True

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)

PROJECT_APPS = (
    'app',
    'busquedas',
    'estadisticas',
    'habilidades',
    'preguntas',
    'respuestas',
    'usuarios',
)

THIRTY_PARTY_APPS = (
    'djrill',
)

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRTY_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# SMTP Settings Backend
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'

MANDRILL_API_KEY = 'Fj_DwFYGpE5IXMS4lua_Hg'
# SMTP Settings Backend




ROOT_URLCONF = 'oportunidapp.urls'

WSGI_APPLICATION = 'oportunidapp.wsgi.application'

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd19nmg8u9k0f6j',
        'USER': 'imxmlamvskvoyi',
        'PASSWORD': '9aiQQ3kfOj5D06Vn4F6SUATg_V',
        'HOST':'ec2-54-225-134-223.compute-1.amazonaws.com',
        'PORT':'5432',
    }
}
#DATABASES['default'] =  dj_database_url.config()

# Enable Connection Pooling (if desired)
#DATABASES['default']['ENGINE'] = 'django_postgrespool'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

LOGIN_URL = '/ingresar'

LOGOUT_URL = '/salir'

STATIC_ROOT = 'staticfiles'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'
