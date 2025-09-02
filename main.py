from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

plugins = dict(root="plugin")
bot = Client("santodelgiorno",
             api_id = 782440,
             api_hash = "ce5ba256fd8298a482e6d847cdfcec94",
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