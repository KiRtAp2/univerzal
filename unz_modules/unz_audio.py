import os
from discord.utils import get
import discord
import asyncio

from . import UnzBaseModule, EventHandlerStatus
import settings as stg


class UnzAudioModule(UnzBaseModule):

    name = "unz-audio"

    default_config = {
        "command": "play",
        "arguement-error": "Please provide track filename",
        "no-voice-channel-error": "You are not in a voice channel",
        "no-such-track-error": "There is no such track in media dir",
        "still-playing-check-interval": 5,
    }

    async def event_on_message(self, message, client):
        if message.guild is None:
            return EventHandlerStatus.PASS

        if message.content.startswith(self.config["command"]+" "):
            cmd, *args = message.content.split()
            if not args:
                await message.channel.send(self.config["arguement-error"])
                return EventHandlerStatus.BLOCK
            track = os.path.join(stg.MEDIA_AUDIO_DIR, args[0])
            if not os.path.exists(track):
                await message.channel.send(self.config["no-such-track-error"])
                return EventHandlerStatus.BLOCK

            member = get(message.guild.members, id=message.author.id)
            if member is None or member.voice is None:
                await message.channel.send(self.config["no-voice-channel-error"])
                return EventHandlerStatus.BLOCK

            audio_src = discord.FFmpegPCMAudio(track)
            voice_channel = await member.voice.channel.connect()
            voice_channel.play(audio_src, after=None)
            while voice_channel.is_playing():
                await asyncio.sleep(self.config["still-playing-check-interval"])
            await voice_channel.disconnect()
