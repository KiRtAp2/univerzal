from . import UnzBaseModule, get_guild_or_channel


class UnzControlModule(UnzBaseModule):

    name = "unz-control"

    def check_data(self):
        if "mute-command" not in self.config:
            self.config["mute-command"] = "unz-mute"

        if "unmute-command" not in self.config:
            self.config["unmute-command"] = "unz-unmute"

        if "mark-channel-command" not in self.config:
            self.config["mark-channel-command"] = "unz-control-mark"

        if "arguement-error-mark-channel" not in self.config:
            self.config["arguement-error-mark-channel"] = "Please provide name for channel"

        if "confirm-message" not in self.config:
            self.config["confirm-message"] = "ok"

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

        if message.content.startswith(self.config["unmute-command"]):
            self.global_data["per-guild"][gcid]["bot-muted"] = False
            if self.config["confirm-message"]:
                await message.channel.send(self.config["confirm-message"])

        if message.content.startswith(self.config["mark-channel-command"]+" "):
            cmd, *args = message.content.split()
            if len(args) < 1:
                await message.channel.send(self.config["arguement-error-mark-channel"])
                return
            else:
                self.global_data["marked-ids"][args[0]] = message.channel.id
                if self.config["confirm-message"]:
                    await message.delete()
