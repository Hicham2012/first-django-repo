"""
WSGI config for littlelemon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
>>>>>>> 8ab6f7f157ca9c8ce9f6d96e5e8891cd544e82f6
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')

application = get_wsgi_application()
