import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ScrumPokerConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        action = data.get("action")

        if action == "vote":
            username = data.get("username", "Anonymous")
            vote = data.get("vote")
            await self.channel_layer.group_send(
                self.room_group_name,
                {"type": "vote_received", "username": username, "vote": vote}
            )
        elif action == "reveal":
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "reveal_votes"}
            )

    async def vote_received(self, event):
        """Sends the received vote message to all connected clients."""
        self.votes[event["username"]] = event["vote"]
        await self.send(text_data=json.dumps(
                {"action": "vote",
                "username": event["username"],
                "vote": "hidden"  # we don't display the vote yet
        }))

    async def reveal_votes(self, event):
        data ={
            "action": "reveal",
            "votes": [{"username": user, "vote": vote} for user, vote in self.votes.items()]
        }
        await self.send(text_data=json.dumps(data))
