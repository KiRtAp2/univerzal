import logging

from . import UnzBaseModule, get_guild_or_channel, EventHandlerStatus
from . import send_message


class UnzAutoreplyModule(UnzBaseModule):

    name = "unz-autoreply"

    default_config = {
        "personalities": []
    }

    def check_data(self):
        if not self.config["personalities"]:
            logging.warning("unz-autoreply has no personalities loaded! it won't do anything")

        if "per-guild" not in self.global_data:
            self.global_data["per-guild"] = {}

        self.personalities = list(sorted(self.config["personalities"], reverse=True))

    async def event_on_message(self, message, client):
        guid = str(get_guild_or_channel(message))
        if guid in self.global_data["per-guild"] and \
           self.global_data["per-guild"][guid].get("bot-muted", False):
            return EventHandlerStatus.PASS
        for p in self.personalities:
            resp = p.trigger(message.content)
            if resp is not None:
                await send_message(message.channel, resp)
                return EventHandlerStatus.BLOCK
        return EventHandlerStatus.PASS
