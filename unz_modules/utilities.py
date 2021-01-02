import discord
import os
from enum import Enum
import logging

import settings as stg


def get_guild_or_channel(message):
    # return guild id if message is in guild, else channel id
    if message.guild is not None:
        return message.guild.id
    else:
        return message.channel.id


def read_file(filename):
    path = os.path.join(stg.MEDIA_FILES_DIR, filename)
    try:
        with open(path) as f:
            data = f.read()
        return data
    except (FileNotFoundError, PermissionError):
        logging.error(f"read_file: Unable to read {filename} in {stg.MEDIA_FILES_DIR}")
        raise


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


class EventHandlerStatus(Enum):
    BLOCK = 1
    PASS = 2
