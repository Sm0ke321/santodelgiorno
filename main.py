from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os

bot_token = os.getenv("BOT_TOKEN")
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

plugins = dict(root="plugin")
bot = Client("santodelgiorno",
             api_id = api_id,
             api_hash = api_hash,
             bot_token = bot_token,
             plugins = plugins)


@bot.on_message(filters.command("start") & filters.incoming & filters.private)
async def start(_, message):
    date = message.date.strftime("%d-%m-%Y")
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎉 Scopri il santo", callback_data="sdg")
        ]
    ])
    await message.reply(f"👋🏼 {message.from_user.mention}, grazie a questo bot potrai ottenere il santo (o i santi) "
                        f"del giorno!\n\n🗓 <b>Data Rilevata:</b> {date}",
                        reply_markup=reply_markup)

bot.run()