from configs import *
from database.database import db
from pyrogram import Client
from pyrogram.types import Message
from bot import mxabot


async def adduser(Client, message: Message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        if LOG_CHANNEL is not None:
            await mxabot.send_message(
                int(LOG_CHANNEL),
                f"#new_user :-\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{BOT_USERNAME}!"
            )


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
