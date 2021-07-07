from .base import *

DEBUG = True
ALLOWED_HOSTS = ['vozt.herokuapp.com']
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hhdk43ojb',
    'API_KEY': '694815981387673',
    'API_SECRET': '4vbHyadSXOCHD5EhhO0SCJ0n2Kc',
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


STRIPE_PUBLIC_KEY = ('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = ('STRIPE_TEST_SECRET_KEY')
