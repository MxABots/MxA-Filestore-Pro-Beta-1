import os
from os import getenv
import logging
import logging.config
import asyncio
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyromod import listen
from pyrogram import Client

API_ID = int(getenv("API_ID", "28376552"))
API_HASH = getenv("API_HASH", "d4ead25e66fc1c4326d533614dad3ecd")
BOT_TOKEN = getenv("BOT_TOKEN", "6399715419:AAEiy2g3YfsdYO2KHd8yC6qy1dNfKrtxg0s")

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

        
if __name__ == "__main__":
    mxabot.main()
