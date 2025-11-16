from telegram.ext import ContextTypes
from utils.downloader import download_media
from bot import ConversationHandler

async def choose_format(update, context: ContextTypes.DEFAULT_TYPE):
    quality = update.message.text
    link = context.user_data.get("link")

    await update.message.reply_text("⬇ Downloading... please wait.")

    try:
        file_path = await download_media(link, quality)
        await update.message.reply_video(video=open(file_path, "rb"))
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

    return ConversationHandler.END
