from telegram import ReplyKeyboardMarkup

async def link_handler(update, context):
    context.user_data["link"] = update.message.text

    keyboard = [["360p", "720p", "1080p", "Audio"]]

    await update.message.reply_text(
        "Choose format/resolution:",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    )

    return 2   # CHOOSING_FORMAT
