import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ScrumPokerConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_name = None
        self.room_group_name = None
        self.votes = {}

    async def connect(self):
        """Handles a new WebSocket connection."""
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"poker_{self.room_name}"

        # Join the WebSocket group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        """Handles WebSocket disconnection."""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        """Receives a vote from a user and broadcasts it to the group."""
        data = json.loads(text_data)
        vote = data.get("vote")
        username = data.get("username", "Anonymous")

        # Send vote to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "vote_message",
                "vote": vote,
                "username": username,
            },
        )

    async def vote_message(self, event):
        """Sends the received vote message to all connected clients."""
        vote = event["vote"]
        username = event["username"]

        # Store usernames and votes
        self.votes[username] = vote

        await self.send(text_data=json.dumps({"username": username, "vote": "voted"}))
