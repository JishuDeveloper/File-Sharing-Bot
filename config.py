import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "6999041304:AAG-3dRIofLGNz6NndhvQJFjSUXs5JzNJl4")
API_ID = int(os.environ.get("API_ID", "25961801"))
API_HASH = os.environ.get("API_HASH", "c9d39e5cba88255416aad52f0d0e1cd8")


OWNER_ID = int(os.environ.get("OWNER_ID", "7031870310"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://piyush2004:piyush2004@cluster0.7w3eadf.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "piyush2004")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002147331271"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002229697177"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[7028183236]
    for x in (os.environ.get("ADMINS", "7028183236").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(7031870310)

LOG_FILE_NAME = "Db_private"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
