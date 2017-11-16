"""
WSGI config for weather project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather.settings")

application = get_wsgi_application()


path = '/Users/manishsinha/coding-django/weather'
if path not in sys.path:
    sys.path.append(path)
