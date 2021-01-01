import discord
import logging
import asyncio

import settings as stg
import db_handler
from module_registry import get_default_registry
from unz_modules.base_module import UnzBaseModule


logging.basicConfig(
    level=stg.LOG_LEVEL,
    format=stg.LOG_FORMAT,
    datefmt=stg.LOG_DATEFMT,
    handlers=[
        logging.FileHandler(
            stg.LOG_FILENAME,
            mode=stg.LOG_FILEMODE
        ),
        logging.StreamHandler()
    ]
)

client = discord.Client()
with open("SECRET") as f:
    SECRET = f.readline().strip()


registry = get_default_registry()
database = db_handler.load_or_create()
UnzBaseModule.global_data = database.get("unz_global", {})
loaded_modules = []
for modname in stg.LOADED_MODULES:
    config = stg.MODULE_CONFIG.get(modname, {})
    loaded_modules.append(registry.get_module(modname)(database, config))


@client.event
async def on_ready():
    app_info = await client.application_info()
    logging.info(f"Client logged in as {app_info.name}")

    for module in loaded_modules:
        await module.event_on_ready(client)


@client.event
async def on_message(message):
    if type(message.channel) == discord.TextChannel:
        log_msg = f"Message :: {message.channel.name} ({message.channel.id}) :: {message.author} ({message.author.id}) :: {message.content}"
    else:
        log_msg = f"Message :: {message.channel.id} :: {message.author} ({message.author.id}) :: {message.content}"
    logging.info(log_msg)
    for module in loaded_modules:
        await module.event_on_message(message, client)


@client.event
async def on_disconnect():
    db_handler.save(database, loaded_modules)


async def db_saver():
    await client.wait_until_ready()
    while not client.is_closed():
        db_handler.save(database, loaded_modules)
        await asyncio.sleep(stg.DB_AUTOSAVE_INTERVAL)


if __name__ == "__main__":
    client.loop.create_task(db_saver())
    client.run(SECRET)
