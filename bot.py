from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import re

TOKEN = "8914917634:AAF4k9h2iu3Y6n0AJAkouh3QsL3YpVO-5-Y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك في TOYS CITY Bot!\n\n"
        "📦 أرسل صورة أو فيديو أو نص."
    )

def remove_price(text):
    if not text:
        return ""

    lines = text.split("\n")
    new_lines = []

    for line in lines:
        l = line.lower()

        if (
            "جنيه" in l
            or "egp" in l
            or "السعر" in l
            or re.search(r"\d+\s*ج", l)
        ):
            continue

        new_lines.append(line)

    return "\n".join(new_lines)
async def receive(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = ""

    if update.message.caption:
        text = update.message.caption

    elif update.message.text:
        text = update.message.text

    text = remove_price(text)

    post = f"""
🔥 جديد في TOYS CITY 🔥

{text}

😍 السعر ولا في الخيال 😍

📩 للتواصل ابعتلنا رسالة.

🏪 TOYS CITY
"""

    if update.message.photo:
        await update.message.reply_photo(
            photo=update.message.photo[-1].file_id,
            caption=post
        )

    elif update.message.video:
        await update.message.reply_video(
            video=update.message.video.file_id,
            caption=post
        )

    else:
        await update.message.reply_text(post)
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(
        filters.TEXT | filters.PHOTO | filters.VIDEO,
        receive,
    )
)

print("Bot is running...")
app.run_polling()
