from telegram.ext import ContextTypes
from bot import GETTING_LINK

async def choose_platform(update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["platform"] = update.message.text
    await update.message.reply_text("📎 Send the media link:")
    return GETTING_LINK
