from pyrogram import Client
from pytgcalls import PyTgCalls

API_ID = 30393757
API_HASH = "61bf9121fd68e732ab283144a0c6169f"
BOT_TOKEN = "8658970682:AAEAVpUdljpJdPFp_QzccNek6yeT52wJua8"

app = Client("musicbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call = PyTgCalls(app)

@app.on_message()
async def start(_, message):
    await message.reply("Bot is running ✅")

app.start()
call.start()
print("Bot Started ✅")
app.idle()
