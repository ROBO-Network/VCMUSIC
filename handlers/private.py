from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME,BOT_USERNAME
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/002151a1eb0040d0b7b90.jpg")
    await message.reply_text(
        f"""**Hey, I'm {BOT_NAME} π
ΞΉ Ο²α΄Ι΄ ΟΚα΄Κ ΠΌα΄ΡΙͺα΄ ΞΉΙ΄ Ξ³α΄α΄Κ gΚα΄α΄α΄© Ξ½α΄Ιͺα΄α΄ Ο²Κα΄α΄. βα΄α΄ α΄Κα΄α΄©α΄α΄ ΟΚ  [γTUSHARγπγROMANTICβ€SHAYARγ](https://t.me/TUSHAR204) .
Ξ±α΄α΄ ΠΌα΄ Οα΄ Ξ³α΄α΄Κ gΚα΄α΄α΄© Ξ±Ι΄α΄ ΟΚα΄Κ ΠΌα΄ΡΙͺα΄ ΖΚα΄α΄ΚΚ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ππππππ", url="t.me/tushar204")
                  ],[
                    InlineKeyboardButton(
                        "ππππππππΏ", url="https://t.me/LOVELYAPPEAL"
                    ),
                    InlineKeyboardButton(
                        "πππππππ", url="https://t.me/ABOUTVEDMAT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "ππππ πππππ", url="https://t.me/LOVELYR_OBOT"
                    )
                ],[
                    InlineKeyboardButton(
                        "βπππ ππ πππππβ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aα΄ OΙ΄ΚΙͺΙ΄α΄ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ππππππππ", url="https://t.me/ABOUTVEDMAT")
                ]
            ]
        )
   )
