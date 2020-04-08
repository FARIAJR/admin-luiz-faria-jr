"""
WSGI config for admin_luiz_faria_jr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static impor Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_luiz_faria_jr.settings')

application = Cling(get_wsgi_application())
