from random import choice as rand_choice

from . import UnzBaseModule, EventHandlerStatus, read_file


class UnzWordsModule(UnzBaseModule):

    name = "unz-words"

    def check_data(self):
        if "dictionary-filename" not in self.config:
            self.config["dictionary-filename"] = "dictionary.txt"

        if "enable-command" not in self.config:
            self.config["enable-command"] = True

        if "command" not in self.config:
            self.config["command"] = "unz-word"

        self.global_config["dictionary"] = \
            read_file(self.config["dictionary-filename"]).splitlines()

    async def event_on_message(self, message, client):
        if self.config["enable-command"]:
            if message.content.startswith(self.config["command"]):
                await message.channel.send(rand_choice(
                    self.global_config["dictionary"]
                ))
                return EventHandlerStatus.BLOCK
