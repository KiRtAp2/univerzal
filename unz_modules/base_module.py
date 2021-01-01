import logging


class UnzBaseModule:

    name = "abstract-base"
    global_data = {}

    def __init__(self, db={}, config={}):
        self.config = config
        if self.name in db:
            self.local_data = db[self.name]
        else:
            self.local_data = {}

        self.check_data()

    @staticmethod
    def get_empty_database(self):
        return {}

    def check_data(self):
        pass

    async def event_on_ready(self, client):
        pass

    async def event_on_message(self, message, client):
        pass

    def get_db(self):
        return self.local_data


class UnzDebugModule(UnzBaseModule):

    name = "debug"

    def check_data(self):
        if "report-on-ready" not in self.config:
            self.config["report-on-ready"] = True

        if "report-on-message" not in self.config:
            self.config["report-on-message"] = True

        logging.debug(f"Debug database: {self.local_data}")

    async def event_on_ready(self, client):
        if self.config["report-on-ready"]:
            msg = "Debug module event_on_ready."
            if "blob" in self.local_data:
                msg += f" blob: {self.local_data['blob']}"
            logging.debug(msg)

    async def event_on_message(self, message, client):
        if self.config["report-on-message"]:
            logging.debug(f"Debug module received message: {message.content}")

        if message.content.startswith("debug_set_blob "):
            blob = message.content.split()[1]
            self.local_data["blob"] = blob

        if message.content.startswith("debug_get_global_data"):
            await message.channel.send(f"{self.global_data}")


def get_guild_or_channel(message):
    # return guild id if message is in guild, else channel id
    if message.guild is not None:
        return message.guild.id
    else:
        return message.channel.id
