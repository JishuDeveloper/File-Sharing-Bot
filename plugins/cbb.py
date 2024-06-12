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
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={1308086294}'>ᴍɪɴᴀᴛᴏ-ꜱᴀᴍᴀ</a>\n○ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/IAS_MOVIESANDSERIES'>Channel</a>\n○ ʀᴇQᴜᴇꜱᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/IAS_MOVIE_CHATS'>Chat</a>\n○ ʙᴀᴄᴋᴜᴘ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+6LZSdAbBv4c0MDVl'>Channel</a></b>",
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
