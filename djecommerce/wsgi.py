from dj_static import Cling
import os

from django.core.wsgi import get_wsgi_application

# se configura los dos por que settings es carpeta y se bsca el local o production o developed
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'djecommerce.settings.production')

#application = get_wsgi_application()

application = Cling(get_wsgi_application())
