"""
WSGI config for smart_mingle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

application = get_wsgi_application()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_mingle.settings')
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))

application = get_wsgi_application()
