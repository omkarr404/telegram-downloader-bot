async def platform_handler(update, context):
    context.user_data["platform"] = update.message.text
    await update.message.reply_text("📎 Send the media link:")
    return 1   # GETTING_LINK
