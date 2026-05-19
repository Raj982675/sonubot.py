from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes,
    CommandHandler
)

import asyncio
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

BOT_TOKEN = "8946964685:AAGWonSuVfwJCdEiBI9iXcxH1tLHvU-YzRk"
YOUR_TELEGRAM_ID = 5833651677

USERS_FILE = "users.txt"

def save_user(user_id):
    try:
        with open(USERS_FILE, "a+") as f:
            f.seek(0)
            users = f.read().splitlines()
            if str(user_id) not in users:
                f.write(f"{user_id}\n")
    except:
        pass

async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request
    user_id = req.from_user.id
    chat_id = req.chat.id

    print(f"🔄 New Join Request from: {user_id}")

    save_user(user_id)

    # ================== STRICT SEQUENCE ==================

    # 1. Welcome Message
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text="""👋 Welcome!

✅ Aapka join request successfully approve ho gaya hai
📢 @𝐃𝐞𝐯_𝐭𝐡𝐞𝐏𝐫𝐞𝐝𝐢𝐜𝐭𝐨𝐫.

📩 Niche diya gaya important hack zarur use karein 👇

🚀 Ye hack aapko better results aur fast growth dene me help karega.

⚠️ Miss mat karna — properly follow karna!

Please wait a moment ⏳"""
        )
        print("✅ Sent 1/5: Welcome")
    except Exception as e:
        print(f"Welcome Error: {e}")

    await asyncio.sleep(1)   # Small delay for better order

    # 2. Video
    try:
        await context.bot.send_video(
            chat_id=user_id,
            video=open("sonu bot video.mp4", "rb"),
            caption="""🎥 Play Karo The_Devpredictor ke sath and nikalo achhi profit daily😍❤️❤️🛍🔔💯🔄
            
http://jgame3.com/#/register?invitationCode=753642914702

Personal Sureshot mil raha hai abhi jinhe chahiye wah mujhe message kariye jaldi 😬👑🏆🌟

🔑🛡@sonu2662""",
            supports_streaming=True
        )
        print("✅ Sent 2/5: Video")
    except Exception as e:
        print(f"Video Error: {e}")

    await asyncio.sleep(1)

    # 3. APK
    try:
        await context.bot.send_document(
            chat_id=user_id,
            document=open("DEV VIP TOOL_1.0.apk", "rb"),
            caption="""𝗛𝗔𝗖𝗞 𝗔𝗽𝗽 ✅
.
👈🔝 ✅
🤝🤝Minimum ₹200 deposit """
        )
        print("✅ Sent 3/5: APK")
    except Exception as e:
        print(f"APK Error: {e}")

    await asyncio.sleep(1)

    # 4. Voice
    try:
        await context.bot.send_voice(
            chat_id=user_id,
            voice=open("sonu voice.mp3", "rb"),
            caption="🎙 Important Voice Message"
        )
        print("✅ Sent 4/5: Voice")
    except Exception as e:
        print(f"Voice Error: {e}")

    await asyncio.sleep(1)

    # 5. Final Text Message
    try:
        await context.bot.send_message(
            chat_id=user_id,
            text="✅ 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝘁𝗶𝗼𝗻 𝗸𝗮𝗿𝗸𝗲 𝗞𝘂𝗰𝗵𝗵 𝗯𝗵𝗶 𝗔𝗺𝗼𝘂𝗻𝘁 𝗗𝗲𝗽𝗼𝘀𝗶𝘁 𝗸𝗮𝗿𝗹𝗼 𝗼𝗼𝘀𝗸𝗲 𝗯𝗮𝗮𝗱 𝗵𝗮𝗺𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗸𝗮𝗿𝗼 𝗨𝗜𝗗 𝗻𝘂𝗺𝗯𝗲𝗿 𝗸𝗲 𝘀𝗮𝘁𝗵, 𝗛𝗮𝗺 𝗮𝗮𝗽𝗸𝗼 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲 𝗔𝗱𝗱 𝗸𝗮𝗿𝗱𝗲𝗻𝗴𝗲  𝗮𝗻𝗱 𝗮𝗮𝗽 𝘄𝗮𝗵𝗮𝗻 𝘀𝗲 𝗮𝗰𝗵𝗵𝗮 𝗽𝗿𝗼𝗳𝗶𝘁 𝗡𝗶𝗸𝗮𝗹𝗻𝗮 💳🪙 🎉"
        )
        print("✅ Sent 5/5: Final Text")
    except Exception as e:
        print(f"Final Text Error: {e}")

    # Auto Approve
    try:
        await context.bot.approve_chat_join_request(
            chat_id=chat_id, user_id=user_id
        )
        print(f"✅ Auto Approved: {user_id}")
    except Exception as e:
        print(f"Approve Error: {e}")


async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != YOUR_TELEGRAM_ID:
        return
    # Broadcast code same rahega (agar chahiye to batao)


async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(join_request))
    app.add_handler(CommandHandler("broadcast", broadcast))

    print("🤖 Bot Started - Strict Order Mode")

    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)

    await asyncio.Event().wait()


asyncio.run(main())