from . import UnzBaseModule, EventHandlerStatus


class UnzMessageModule(UnzBaseModule):

    name = "unz-message"

    default_config = {
        "command": "unz-message",
        "arguement-error": "Too few arguements. Use unz-message (channel-name) (message)",
        "channel-error": "Unknown channel"
    }

    def check_data(self):
        if "marked-ids" not in self.global_data:
            self.global_data["marked-ids"] = {}

    async def event_on_message(self, message, client):
        if message.content.startswith(self.config["command"]+" "):
            cmd, *args = message.content.split()
            if len(args) < 1:
                await message.channel.send(self.config["arguement-error"])
                return EventHandlerStatus.BLOCK
            chn_name = args[0]
            if chn_name not in self.global_data["marked-ids"]:
                await message.channel.send(self.config["channel-error"])
                return EventHandlerStatus.BLOCK
            channel = client.get_channel(self.global_data["marked-ids"][chn_name])
            msg = " ".join(args[1:])
            if message.attachments:
                atchn = message.attachments[0]
                fileobj = await atchn.to_file()
                await channel.send(msg, file=fileobj)
            else:
                await channel.send(msg)
            return EventHandlerStatus.BLOCK
