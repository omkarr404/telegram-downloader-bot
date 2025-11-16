import os
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ConversationHandler
)

from handlers.start_handler import start_handler
from handlers.platform_handler import platform_handler
from handlers.link_handler import link_handler
from handlers.format_handler import format_handler

BOT_TOKEN = os.getenv("BOT_TOKEN")

# States
CHOOSING_PLATFORM, GETTING_LINK, CHOOSING_FORMAT = range(3)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start_handler)],
        states={
            CHOOSING_PLATFORM: [MessageHandler(filters.TEXT, platform_handler)],
            GETTING_LINK: [MessageHandler(filters.TEXT, link_handler)],
            CHOOSING_FORMAT: [MessageHandler(filters.TEXT, format_handler)]
        },
        fallbacks=[]
    )

    app.add_handler(conv)

    print("Bot started!")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
