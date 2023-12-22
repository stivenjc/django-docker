from django.urls import path
from apps.chat import consumers


websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', consumers.chatConsumers.as_asgi())
]