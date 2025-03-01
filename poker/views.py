from django.shortcuts import render

def poker_room(request, room_name):
    """Render the Scrum Poker room with WebSocket support."""
    return render(request, "poker/room.html", {"room_name": room_name})