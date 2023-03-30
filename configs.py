# (c) @AM_ROBOTS

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 24736263))
    API_HASH = os.environ.get("API_HASH", "4d53732917b73a6bb89c3b2f2f7b0902")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6182691772:AAGlpYbgFr2dONr7JZS6nqxo-imEBWSie6k")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQCf2IZcevoMCNQVL17rlYGjv46W54x68KnhkgxxMWWDgNP05tp8IacJ66NJcS_ORXTAbfx9h2Kmr8DoRFJ0-r7rncxE_9I5itJsgMRU-aBB91l4Ia7bnQPjhNVIEZYKXLYjEXIkjH7BmbMrvfcXD0eUQICWEnbvC27XoPc6xVcrxvzSA0RncQx7MaFL9kRxj5xkTtHqRHbzyqgfC38PzMG-s9DcBa4_FILLGfyO5Sj0r6b0ctBgVF3n1dyDlBK8p7IX-Z19lwfL-mQSB87szAYf_v-aeMAqMFje_nS1rkAKkUaKpeYKTi3mJDZj7DU23_lK7QAc_fgxVZ_RfiJhIcEwAAAAATlllSEA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001895151847))
    BOT_USERNAME = os.environ.get("Nancyautofilter_bot")
    BOT_OWNER = int(os.environ.get("5257925921"))
    DATABASE_URL = os.environ.get("mongodb+srv://nancyhub4vf:bhargavp1209@cluster0.l767a8r.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/nvslinkbot'>Lin Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/tgnvs'>TGNVS</a></b>
"""

    ABOUT_HELP_TEXT = """<b>Donation</b>
<b>Thanks for showing interest in donation
Donate Us To Keep Alive
Continously Alive

You Can Send Any Amount
Donate Only One Rupee
Of 10₹,20₹,30₹,50₹,100₹ 😁

💸Payment Methods:
Only UPI
UPI:-</b> tgnvs@airtel
-<b> <a href=https://upier.vercel.app/pay/tgnvs@airtel?am=15>Donation Link</a></b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @tgnvs</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @tgnvs</a></b>
"""

