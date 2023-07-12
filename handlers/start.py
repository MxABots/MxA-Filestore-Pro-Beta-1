from configs import *
from pyrogram import Client
from pyrogram.types import Message

async def start(client, message):
    await handle_private_message(client, message)
    await message.delete()
    fsub = await force_sub(client, message)
    if fsub == 400:
        return
    await message.reply_text(
        START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Dev 👨‍💻", user_id="6112935306"),
                    InlineKeyboardButton("Close ❌", callback_data="delete")
                ]
            ]
        )
    )
