# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u*jztkbawo=dt(df0ofb^!z83+y1!+6*&n%c0xm-s%e%4&24qe'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}