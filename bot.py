import os
from os import getenv
import logging
import logging.config
import asyncio
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyromod import listen
from pyrogram import Client
from pyrogram.types import BotCommand

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

class mxabot(Client):
    def main():
        plugins = dict(root="plugins")
        app = Client("NG_FileStoreBot",
                     bot_token=BOT_TOKEN,
                     api_id=API_ID,
                     api_hash=API_HASH,
                     plugins=plugins,
                     workers=300,
                     sleep_threshold=10,
                     in_memory=True
                    )
        app.run()

commands = [
    BotCommand("start", "Start the bot"),
    #BotCommand("help", "Get help and instructions"),
    #BotCommand("settings", "Change bot settings")
]

mxabot.set_bot_commands(commands)

if __name__ == "__main__":
    mxabot.main()
