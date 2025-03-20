import re
import os
import time

id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "28987210")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "04f69b63570297dac4e35948e4c6b4b7")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7819649400:AAHrXcfn6Wb6gLAU12ASyqf0q6TktsSFH7M")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "28987210")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "04f69b63570297dac4e35948e4c6b4b7")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://sujoy123m:wTWKGUaxYE7dxb1l@cluster0.zorxb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://ibb.co/spZf17n5")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '8181241262').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "supertopperschannel") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002474879896"))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class Txt(object):
    # part of text configuration
    START_TXT = """<b>ʜᴇʏ {}!✨

🫧 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴠᴀɴᴄᴇᴅ ʀᴇɴᴀᴍᴇ ʙᴏᴛ!
ᴡʜɪᴄʜ ᴄᴀɴ ᴍᴀɴᴜᴀʟʟʏ ʀᴇɴᴀᴍᴇ ʏᴏᴜʀ ғɪʟᴇs ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴛʜᴜᴍʙɴᴀɪʟ ᴏɴ ʏᴏᴜʀ ғɪʟᴇs.⚡️

✨ ᴛʜɪs ʙᴏᴛ ɪs ᴅᴇᴘʟᴏʏᴇᴅ ʙʏ Sᴜᴊᴏʏ
──────────────────────
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ  ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.
"""

    ABOUT_TXT = """<b>
╔════❰ Rᴇɴᴀᴍᴇʀ ʙᴏᴛ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃ʙᴏᴛ : [Rᴇɴᴀᴍᴇʀ Bᴏᴛ](https://t.me/ToppersRenamer_Bot)
║┣⪼👦Cʀᴇᴀᴛᴏʀ : [Sᴜᴊᴏʏ 👑](https://t.me/UncleChipssBot)
║┣⪼🤖Uᴘᴅᴀᴛᴇ : [Sᴜᴘᴇʀ Tᴏᴘᴘᴇʀs](https://t.me/SuperToppers)
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : Sᴜᴘᴇʀ Fᴀsᴛ
║┣⪼🗣️Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
║┣⪼📚Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ Gᴀᴛʜᴇʀ 2.31.0 
║┣⪼🗒️Vᴇʀsɪᴏɴ : 2.18.3
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
</b>"""

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴʏ Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ Sᴇᴛ Tʜᴜᴍʙɴᴀʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴᴀʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ: <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tʏᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ Aɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:

◦ <code>Telegram : @KPSBots</code>
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱
🗃️ sɪᴢᴇ: {1} | {2}
⏳️ ᴅᴏɴᴇ : {0}%
🚀 sᴘᴇᴇᴅ: {3}/s
⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━ </b>"""
