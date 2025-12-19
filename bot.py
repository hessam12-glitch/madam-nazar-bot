from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8451178063:AAFi7EJbg_6D1iiSNJKpQWwE4UQX0BbfI1A"

IMAGE_URL = "https://example.com/nazar.jpg"
LOCATION_TEXT = "📍 موقع مدام نزار اليوم في Red Dead Online"

async def reply_nazar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and "نزار" in update.message.text:
        await update.message.reply_photo(
            photo=IMAGE_URL,
            caption=LOCATION_TEXT
        )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_nazar))
    print("Madam Nazar Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
