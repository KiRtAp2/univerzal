import logging

from . import UnzBaseModule, EventHandlerStatus


class UnzAutomessageModule(UnzBaseModule):

    name = "unz-automessage"

    default_config = {
        "interval": 0,
        "message": "",
        "channel-mark": "",
    }

    def check_data(self):
        self.secondary_interval = self.config["interval"]

    async def loop_function(self, client):
        chid = self.global_data["marked-ids"].get(self.config["channel-mark"], None)
        if chid is None:
            logging.error(f"Cannot find channel ID with mark {self.config['channel-mark']}")
            return
        channel = client.get_channel(chid)
        if channel is None:
            logging.error(f"Channel with mark {self.config['channel-mark']} does not exist")
            return

        await channel.send(self.config["message"])
