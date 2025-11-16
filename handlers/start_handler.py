from telegram import ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from bot import CHOOSING_PLATFORM

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Instagram", "YouTube"]]

    await update.message.reply_text(
        "👋 Welcome to the Media Downloader Bot!\n\nSelect a platform:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )
    return CHOOSING_PLATFORM
