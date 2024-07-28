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
            text="😈 𝙾𝙽𝚆𝙴𝚁 😈",url="http://t.me/mrdevil12"
        ),
    ],
    [
        InlineKeyboardButton(text="𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url="https://t.me/devilbots971"),
        InlineKeyboardButton(text="𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿", url="https://t.me/devilbotsupport"),
    ],
    [
        InlineKeyboardButton(text="𝙲𝙷𝙰𝚃 𝙶𝚁𝙾𝚄𝙿",= url="https://t.me/akatsuki976"),
    ])


@Client.on_message(filters.command("start"))
async def start(_, ryui: Message):
    user_and_chats = ryui.from_user.first_name
    await ryui.reply_photo(
        "https://graph.org/file/5184a670042b456f1085f.jpg",
        reply_markup=joinButton,
        caption=f"""𝐇𝐞𝐥𝐥𝐨 𝐈𝐚𝐦 𝐃𝐄𝐕𝐈𝐋 𝐗 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐏𝐇
            𝐇𝐎𝐖 𝐀𝐑𝐄 𝐘𝐎𝐔 **__`{user_and_chats}`__**,
           
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


🖥ᴛʜɪꜱ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ @mrdevil12 | ꜰᴏʀ ꜱᴜᴘᴘᴏʀᴛ ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ @devilbotsupport""")
    raise StopPropagation
