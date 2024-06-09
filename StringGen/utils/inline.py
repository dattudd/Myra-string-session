from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="ɢᴇɴᴇʀᴀᴛᴇ 𝘀ᴇ𝘀𝘀ɪᴏɴ", callback_data="gensession")],
        [
            InlineKeyboardButton(text="ᴛʜᴀɴᴜ ꜱᴇʀᴠᴇʀ", url="https://t.me/Thanuserver_op"
            [InlineKeyboardButton(text="𝗢𝘄𝗻𝗲𝗿", url="https://t.me/BTSChinna_op")
            ),
       ],
    ]
(

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍv2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
