from .base import *

DEBUG = True
ALLOWED_HOSTS = ['los4leones.herokuapp.com']
# 'vozt.herokuapp.com'

# AUTH_PASSWORD_VALIDATORS = [
#   {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#  {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
# {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
# ]


#import dj_database_url
#from decouple import config


#db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd13gq8q678e41u',
        'USER': 'vnesnqygvhswzo',
        'PASSWORD': '05dcffa1be2a447075fb1ff23064efa085edd98504e6117910c897f4ed921ece',
        'HOST': 'ec2-52-86-25-51.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}
#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.postgresql_psycopg2',
   #     'NAME': 'ddeoclis9js5ob',
    #    'USER': 'gfvkujtrxdwdiv',
    #    'PASSWORD': '64ac4d5b4daf1548b07a3731f3e8bfe518032f3ea01eafd2c9768cbe0d8998c0',
     #   'HOST': 'ec2-54-88-130-244.compute-1.amazonaws.com',
      #  'PORT': 5432,
    #}
#}




STATICFILES_DIRS = (BASE_DIR, 'static_in_env')
#STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# com esto se actibvan los archivos estaticos para que mejora la vista

#STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
#STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hhdk43ojb',
    'API_KEY': '694815981387673',
    'API_SECRET': '4vbHyadSXOCHD5EhhO0SCJ0n2Kc',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STRIPE_PUBLIC_KEY = ('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = ('STRIPE_TEST_SECRET_KEY')
