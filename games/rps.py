from random import choice as rand_choice

from unz_modules import UnzBaseModule, EventHandlerStatus


class RPSModule(UnzBaseModule):

    name = "rps"

    default_config = {
        "command": "rps",
        "arguement-error": "Usage: rps (rock/paper/scissors)",
        "computer-choice-message": "I choose... {}",
        "player-win-message": "You won",
        "computer-win-message": "I won",
        "tie-message": "It's a tie",
        "paper": "paper",
        "scissors": "scissors",
        "rock": "rock",
    }

    def check_data(self):
        self.choices = (
            self.config["paper"],
            self.config["scissors"],
            self.config["rock"]
        )
        self.rps_beats = {
            self.config["paper"]: self.config["scissors"],
            self.config["scissors"]: self.config["rock"],
            self.config["rock"]: self.config["paper"]
        }

    async def event_on_message(self, message, client):
        if message.content.startswith(self.config["command"]+" "):
            cmd, *args = message.content.split()
            if not args:
                await message.channel.send(self.config["arguement-error"])
                return EventHandlerStatus.BLOCK

            player_choice = args[0].lower()
            if player_choice not in self.choices:
                await message.channel.send(self.config["arguement-error"])
                return EventHandlerStatus.BLOCK

            computer_choice = rand_choice(self.choices)
            await message.channel.send(
                self.config["computer-choice-message"].format(computer_choice)
            )

            if player_choice == self.rps_beats[computer_choice]:
                await message.channel.send(self.config["player-win-message"])
            elif player_choice == computer_choice:
                await message.channel.send(self.config["tie-message"])
            else:
                await message.channel.send(self.config["computer-win-message"])
            return EventHandlerStatus.BLOCK
