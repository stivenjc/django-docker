from django.urls import re_path
from apps.chat import consumers


websocket_urlpatterns = [
    re_path(r'ws/test/$', consumers.testConsumer.as_asgi()),
]