# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'las*-_9l^q&638dajyp6+xb4z03381z3nr2=&dl-l_o((ei4%0'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'NAME': 'shop',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': '0158',
        'OPTIONS': {
          #'autocommit': True,
        },
    }
}

STATICFILES_DIRS = (
    '/home/luis/shop/statics/',
    #'C:\CantoApps\canto\canto\static',
)

TEMPLATE_DIRS = [
    'templates',
]

LOCALE_PATHS = (
    '/home/luis/Documentos/github/shop/locale',
)