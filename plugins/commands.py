from bot import mxabot
from handlers.adduser import adduser
from handlers.start import start
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    Message
)
from plugins.forcesub import force_sub

START_TEXT = '''Hᴇʟʟᴏ {}, I Aᴍ MxA Pɪᴍɪᴜᴍ Fɪʟᴇsᴛᴏʀᴇ Bᴏᴛ!'''

async def handle_private_message(client: Client, message: Message):
    await adduser(client, message)

@mxabot.on_message(filters.command('start'))
async def st(client, message):
    await start(client, message):
