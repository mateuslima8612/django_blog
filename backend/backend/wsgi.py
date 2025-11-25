import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()

# WhiteNoise configuration for static files
application = WhiteNoise(application, root="staticfiles")

# For Vercel
app = application