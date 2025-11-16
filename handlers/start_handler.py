from telegram import ReplyKeyboardMarkup

async def start_handler(update, context):
    keyboard = [["Instagram", "YouTube"]]

    await update.message.reply_text(
        "👋 Welcome!\nSelect a platform:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )

    return 0   # CHOOSING_PLATFORM
