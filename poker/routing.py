from django.urls import re_path
from poker.consumers import ScrumPokerConsumer

websocket_urlpatterns = [
    re_path(r"ws/poker/(?P<room_name>\w+)/$", ScrumPokerConsumer.as_asgi()),
]
