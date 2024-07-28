from pyrogram import StopPropagation
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from pyrogram import Client, filters


joinButton = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʀᴇᴘᴏ", callback_data="SOURCE"),
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅ", callback_data="HELP"),
    ])


@Client.on_message(filters.command("start"))
async def start(_, ryui: Message):
    user_and_chats = ryui.from_user.first_name
    await ryui.reply_photo(
        "https://telegra.ph/file/e26f9a6f0082b4171b6ef.jpg",
        reply_markup=joinButton,
        caption=f"""╰☆☆••| 𝗜𝗺𝗮𝗴𝗲 𝟮 𝗨𝗥𝗟 |••☆☆╮
            𝐇𝐨𝐰𝐝𝐲 **__`{user_and_chats}`__**,
           
🏷 ɪᴍᴀɢᴇ ᴛᴏ ᴜʀʟ ʙᴏᴛ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ᴛʜᴇꜱᴇ ʙᴇʟᴏᴡ ꜰɪʟᴇ ᴛʏᴘᴇꜱ ᴛᴏ [ᴛᴇʟᴇɢʀᴀᴘʜ](https://pypi.org/project/telegraph/) ᴜʀʟ.
🏷 ᴊᴜꜱᴛ ꜱᴇɴᴅ ᴘʜᴏᴛᴏ ᴇɪᴛʜᴇʀ ɪɴ ᴄᴏᴍᴘʀᴇꜱꜱᴇᴅ ᴏʀ ᴜɴᴄᴏᴍᴘʀᴇꜱꜱᴇᴅ ꜰᴏʀᴍᴀᴛ
- `JPG`
- `JPEG`
- `PNG`
- `GIF` __(send as a document)__
- `Mp4` __(send as a document)__
- `Mp3` __(send as a document)__
🏷 ᴋᴇᴇᴘ ꜱᴇɴᴅɪɴɢ ʏᴏᴜʀ ʀᴇQᴜɪʀᴇᴅ ᴛʏᴘᴇ ꜰɪʟᴇꜱ ᴏɴᴇ ʙʏ ᴏɴᴇ.
🏷 ꜰɪʟᴇꜱ ᴍᴏʀᴇ ᴛʜᴇɴ 5ᴍʙ ɪꜱ ɴᴏᴛ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ʙʏ ᴛᴇʟᴇɢʀᴀᴘʜ.


🖥 Dҽʋ Mҽɳƚισɳ: @Krakinz | @KrakinzBot
╰☆☆••| 𝗜𝗺𝗮𝗴𝗲 𝟮 𝗨𝗥𝗟 |••☆☆╮""")
    raise StopPropagation
