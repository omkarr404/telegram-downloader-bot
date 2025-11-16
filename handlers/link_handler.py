from telegram import ReplyKeyboardMarkup
from bot import CHOOSING_FORMAT

async def receive_link(update, context):
    context.user_data["link"] = update.message.text.strip()

    keyboard = [["360p", "720p", "1080p", "Audio"]]

    await update.message.reply_text(
        "Choose format/resolution:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )

    return CHOOSING_FORMAT
