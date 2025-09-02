from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultPhoto, InputTextMessageContent
from pyrogram import Client, filters
from utils import ottieniSanti

@Client.on_callback_query(filters.regex("sdg"))
async def sdg(_, callback_query):
    santo = await ottieniSanti(False)
    await callback_query.message.delete()

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Torna alla home", "restart")]])
    await _.send_photo(chat_id=callback_query.from_user.id,
                       photo= santo['santodelgiorno']['img'],
                       caption= f"🎉 Il santo di oggi è <b>{santo['santodelgiorno']['name']}</b>!\n\n<i>Torna domani per scoprire il prossimo santo!</i>",
                       reply_markup=reply_markup)

@Client.on_callback_query(filters.regex("restart"))
async def restart(_, callback_query):
    await callback_query.message.delete()

    date = callback_query.message.date.strftime("%d-%m-%Y")
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎉 Scopri il santo", callback_data="sdg")
        ]
    ])
    await _.send_message(chat_id= callback_query.from_user.id,
                         text= f"👋🏼 {callback_query.from_user.mention}, grazie a questo bot potrai ottenere il santo (o i santi) del giorno!\n\n🗓 <b>Data Rilevata:</b> <quote>{date}</quote>",
                        reply_markup=reply_markup)