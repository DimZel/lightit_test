"""
WSGI config for lightit_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
from whitenoise.django import DjangoWhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lightit_test.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
