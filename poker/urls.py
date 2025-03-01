from django.urls import path
from poker.views import poker_room

urlpatterns = [
    path("poker/<str:room_name>/", poker_room, name="poker_room"),
]