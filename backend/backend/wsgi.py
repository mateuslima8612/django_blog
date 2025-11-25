"""
WSGI project for backend.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
BASE_DIR = Path(__file__).resolve().parent.parent

application = get_wsgi_application()
# serve collected files from STATIC_ROOT
application = WhiteNoise(application, root=str(BASE_DIR / 'staticfiles'))