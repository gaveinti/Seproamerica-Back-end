from django.urls import re_path
from . import consumers

UUID_CANAL_REGEX=r'ws/chat/(?P<pk>[a-f0 -9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'

websocket_urlpatterns=[
    re_path(r'ws/chat/(?P<room_name>\w+)/$',consumers.chatConsumers.as_asgi())
]