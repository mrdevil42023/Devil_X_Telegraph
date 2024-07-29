import os
import uuid
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from auth import Vauth
from telegraph import upload_file
from pyrogram import StopPropagation
import shutil
EX = "HENTAI"


@Client.on_message(filters.document)
async def getimage(client, message):
    tmp = os.path.join(EX, str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    img_path = os.path.join(tmp, str(uuid.uuid4()) + ".png")
    vid = await message.reply_text("Uploading to my server and analyzing...", True)
    img_path = await client.download_media(message=message, file_name=img_path)
    await vid.edit_text("📷")
    await vid.edit_text("📸")
    await vid.edit_text("🌆")
    await vid.edit_text("📨𝐒𝐞𝐧𝐝𝐢𝐧𝐠 𝐃𝐞𝐬𝐢𝐫𝐞𝐝 𝐋𝐢𝐧𝐤.......")
    try:
        response = upload_file(img_path)
    except Exception as e:
        await vid.edit_text(f"{e}\n\nReport to @devilbots971 or @mrdevil12\n𝗜𝗺𝗮𝗴𝗲 𝟮 𝗨𝗥𝗟 |••☆☆╮")
        await message.reply_text("Retry in few seconds")
        return
    await vid.edit_text(
        text=f"""<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n🖥 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙸𝚂 𝙲𝚁𝙴𝙰𝚃𝙴𝙳 𝙱𝚈 [𝙈𝙍 𝘿𝙀𝙑𝙄𝙇](http://t.me/mrdevil12)
𝙵𝙾𝚁 𝚄𝙿𝙳𝙰𝚃𝙴 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻  [𝘿𝙀𝙑𝙄𝙇 𝘽𝙊𝙏'𝙎](https://t.me/devilbots971)""",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="👓『 𝗦𝗵𝗮𝗿𝗲 』👓",
                url=f"https://telegram.me/share/url?url=https://telegra.ph{response[0]}"),
        ]]))
    try:
        shutil.rmtree(f"DevilxTelegraph/{EX}")
        shutil.rmtree(EX)
    except Exception:
        pass
    raise StopPropagation
