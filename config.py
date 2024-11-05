from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "20798317"))
API_HASH = getenv("API_HASH", "82a94d416e05ca5cc3bc04da8494d7ca")

BOT_TOKEN = getenv("BOT_TOKEN", "7631324434:AAFAUAmFrf1Q9himqaNCzwMr8Wre98zuXyc")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

OWNER_ID = int(getenv("OWNER_ID",  6896043885)))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Thanuserver_op")
