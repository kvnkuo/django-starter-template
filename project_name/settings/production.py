import os
from .base import *

DEBUG = False
TEMPLATE_DEBUG = False

## DATABASE SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}


SECRET_KEY = os.environ['DJANGO_SETTINGS_MODULE']

## WSGI SETTINGS
# https://docs.djangoproject.com/en/1.8/ref/settings/#wsgi-application
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

## NOTIFICATIONS
# A tuple that lists people who get code error notifications.
# https://docs.djangoproject.com/en/1.8/ref/settings/#admins
ADMINS = (
#    ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS


try:
    from local import *
except ImportError:
    pass