from . import UnzBaseModule, EventHandlerStatus


class UnzQuitModule(UnzBaseModule):

    name = "unz-quit"

    default_config = {
        "quit-command": "unz-quit",
        "confirm-message": "ok"
    }

    async def event_on_message(self, message, client):
        if message.content.startswith(self.config["quit-command"]):
            if self.config["confirm-message"]:
                await message.channel.send(self.config["confirm-message"])
            await client.close()
            return EventHandlerStatus.BLOCK
