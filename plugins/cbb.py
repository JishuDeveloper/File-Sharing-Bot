# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={1308086294}'>ᴍɪɴᴀᴛᴏ-ꜱᴀᴍᴀ</a>\n○ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+WHsaD_54uApiMDJl'>ɪᴀꜱ: ᴍᴏᴠɪᴇꜱᴀɴᴅꜱᴇʀɪᴇꜱ</a>\n○ ʙᴀᴄᴋᴜᴘ : <a href='https://t.me/+6LZSdAbBv4c0MDVl'>ɪᴀꜱ ᴍ&ꜱ ʙᴀᴄᴋᴜ</a>\n○ ɢʀᴏᴜᴘ : <a href='https://t.me/+0qJVE9L4pPhhNWM1'>ɪᴀꜱ ᴄʜᴀᴛ ɢʀᴏᴜᴘ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
