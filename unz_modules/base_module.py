import logging

from . import EventHandlerStatus


class UnzBaseModule:

    name = "abstract-base"
    global_data = {}
    global_config = {}

    default_config = {}

    def __init__(self, db={}, config={}):
        self.config = config
        if self.name in db:
            self.local_data = db[self.name]
        else:
            self.local_data = {}

        self.check_config()
        self.check_data()

    @staticmethod
    def get_empty_database(self):
        return {}

    def check_config(self):
        for key, val in self.default_config.items():
            if key not in self.config:
                self.config[key] = val

    def check_data(self):
        pass

    async def event_on_ready(self, client):
        return EventHandlerStatus.PASS

    async def event_on_message(self, message, client):
        return EventHandlerStatus.PASS

    def get_db(self):
        return self.local_data


class UnzDebugModule(UnzBaseModule):

    name = "debug"

    default_config = {
        "report-on-ready": True,
        "report-on-message": True
    }

    def check_data(self):
        logging.debug(f"Debug database: {self.local_data}")

    async def event_on_ready(self, client):
        if self.config["report-on-ready"]:
            msg = "Debug module event_on_ready."
            if "blob" in self.local_data:
                msg += f" blob: {self.local_data['blob']}"
            logging.debug(msg)
        return EventHandlerStatus.PASS

    async def event_on_message(self, message, client):
        if self.config["report-on-message"]:
            logging.debug(f"Debug module received message: {message.content}")

        if message.content.startswith("debug_set_blob "):
            blob = message.content.split()[1]
            self.local_data["blob"] = blob

        if message.content.startswith("debug_get_global_data"):
            await message.channel.send(f"{self.global_data}")
        return EventHandlerStatus.PASS
