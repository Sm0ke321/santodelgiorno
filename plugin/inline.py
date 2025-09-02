from pyrogram import Client
from pyrogram.types import InlineQueryResultPhoto, InputTextMessageContent
from utils import ottieniSanti

@Client.on_inline_query()
async def answer(_, inline_query):
    santi = await ottieniSanti(True)
    result = []

    for nome, info in santi['santodelgiorno'].items():
        result.append(
            InlineQueryResultPhoto(
                photo_url=info['img'],
                title=nome,
                description=f"Mostra {nome}",
                thumb_url=info['img'].replace("big","small"),
                input_message_content=InputTextMessageContent(
                    f"🎉 <b>Oggi si festeggia anche {nome}!</b>"
                )
            )
        )

    await inline_query.answer(results=result, cache_time=1, is_gallery=True)
