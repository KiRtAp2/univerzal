import discord
import os

import settings as stg


def get_guild_or_channel(message):
    # return guild id if message is in guild, else channel id
    if message.guild is not None:
        return message.guild.id
    else:
        return message.channel.id


async def send_message(channel, message, **kwargs):
    if callable(message):
        message = message()
    if message.startswith("!img "):
        cmd, *args = message.split()
        if not args:
            raise ValueError("Image must be provided")
        filename = args[0]
        message = " ".join(args[1:])
        await channel.send(message.format(**kwargs), file=discord.File(
            os.path.join(stg.MEDIA_IMAGES_DIR, filename)
        ))
    else:
        await channel.send(message.format(**kwargs))
