from . import UnzBaseModule, EventHandlerStatus


class UnzMessageModule(UnzBaseModule):

    name = "unz-message"

    def check_data(self):
        if "command" not in self.config:
            self.config["command"] = "."

        if "argument-error" not in self.config:
            self.config["argument-error"] = \
                f"Too few arguments. Use {self.config['command']} (channel-name) (message)"

        if "channel-error" not in self.config:
            self.config["channel-error"] = "Unknown channel"

        if "marked-ids" not in self.global_data:
            self.global_data["marked-ids"] = {}

    async def event_on_message(self, message, client):
        if message.content.startswith(self.config["command"]+" "):
            cmd, *args = message.content.split()
            if len(args) < 1:
                await message.channel.send(self.config["argument-error"])
                return EventHandlerStatus.BLOCK
            chn_name = args[0]
            if chn_name not in self.global_data["marked-ids"]:
                await message.channel.send(self.config["channel-error"])
                return EventHandlerStatus.BLOCK
            channel = client.get_channel(self.global_data["marked-ids"][chn_name])
            await channel.send(" ".join(args[1:]))
