from . import UnzBaseModule


class UnzQuitModule(UnzBaseModule):

    name = "unz-quit"

    def check_data(self):
        if "quit-command" not in self.config:
            self.config["quit-command"] = "unz-quit"

        if "confirm-message" not in self.config:
            self.config["confirm-message"] = "ok"

    async def event_on_message(self, message, client):
        if message.content.startswith(self.config["quit-command"]):
            if self.config["confirm-message"]:
                await message.channel.send(self.config["confirm-message"])
            await client.close()
