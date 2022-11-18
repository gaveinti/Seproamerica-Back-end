"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from django.core.asgi import get_asgi_application
import chat.routing
from starlette.middleware.cors import CORSMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': OriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        ),
        ["*"],
 
    )
})


#application = CORSMiddleware(application, allow_origins=['*'])
