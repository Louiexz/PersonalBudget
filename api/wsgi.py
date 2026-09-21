import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

# Padrão Django: a variável se chama 'application'
application = get_wsgi_application()