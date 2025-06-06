from django.urls import re_path
from .consumers import ContactConsumer

websocket_urlpatterns = [
    re_path(r'^ws/contact/$', ContactConsumer.as_asgi()),
]