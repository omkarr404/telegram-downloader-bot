from utils.downloader import download_media
from telegram.ext import ConversationHandler

async def format_handler(update, context):
    quality = update.message.text
    url = context.user_data["link"]

    await update.message.reply_text("⬇ Downloading... Please wait...")

    try:
        file_path = await download_media(url, quality)
        await update.message.reply_video(open(file_path, "rb"))
    except Exception as e:
        await update.message.reply_text(str(e))

    return ConversationHandler.END
