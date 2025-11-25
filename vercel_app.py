import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()

static_root = os.path.join(os.path.dirname(__file__), 'backend', 'staticfiles')
application = WhiteNoise(application, root=static_root)

app = application