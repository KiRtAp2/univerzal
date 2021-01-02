from . import UnzBaseModule, get_guild_or_channel, EventHandlerStatus


class UnzControlModule(UnzBaseModule):

    name = "unz-control"

    default_config = {
        "mute-command": "unz-mute",
        "unmute-command": "unz-unmute",
        "mark-channel-command": "unz-control-mark",
        "arguement-error-mark-channel": "Please provide name for channel",
        "confirm-message": "ok",
    }

    def check_data(self):
        if "per-guild" not in self.global_data:
            self.global_data["per-guild"] = {}

        if "marked-ids" not in self.global_data:
            self.global_data["marked-ids"] = {}

    async def event_on_message(self, message, client):
        gcid = str(get_guild_or_channel(message))
        if gcid not in self.global_data["per-guild"]:
            self.global_data["per-guild"][gcid] = {}

        if message.content.startswith(self.config["mute-command"]):
            self.global_data["per-guild"][gcid]["bot-muted"] = True
            if self.config["confirm-message"]:
                await message.channel.send(self.config["confirm-message"])
            return EventHandlerStatus.BLOCK

        if message.content.startswith(self.config["unmute-command"]):
            self.global_data["per-guild"][gcid]["bot-muted"] = False
            if self.config["confirm-message"]:
                await message.channel.send(self.config["confirm-message"])
            return EventHandlerStatus.BLOCK

        if message.content.startswith(self.config["mark-channel-command"]+" "):
            cmd, *args = message.content.split()
            if len(args) < 1:
                await message.channel.send(self.config["arguement-error-mark-channel"])
                return EventHandlerStatus.BLOCK
            else:
                self.global_data["marked-ids"][args[0]] = message.channel.id
                if self.config["confirm-message"]:
                    await message.delete()

            return EventHandlerStatus.BLOCK
