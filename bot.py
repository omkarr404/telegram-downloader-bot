# import os
# from telegram.ext import (
#     ApplicationBuilder, CommandHandler, MessageHandler,
#     filters, ConversationHandler
# )

# from handlers.start_handler import start
# from handlers.platform_handler import choose_platform
# from handlers.link_handler import receive_link
# from handlers.format_handler import choose_format

# BOT_TOKEN = "8110654234:AAHawXh47X84oomkTli46StSgWtDUBSmF1w"

# # States
# CHOOSING_PLATFORM, GETTING_LINK, CHOOSING_FORMAT = range(3)


# async def main():
#     app = ApplicationBuilder().token(BOT_TOKEN).build()

#     conv_handler = ConversationHandler(
#         entry_points=[CommandHandler("start", start)],
#         states={
#             CHOOSING_PLATFORM: [MessageHandler(filters.TEXT, choose_platform)],
#             GETTING_LINK: [MessageHandler(filters.TEXT, receive_link)],
#             CHOOSING_FORMAT: [MessageHandler(filters.TEXT, choose_format)],
#         },
#         fallbacks=[]
#     )

#     app.add_handler(conv_handler)

#     print("Bot is running...")
#     await app.run_polling()


# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())


import os
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ConversationHandler
)

from handlers.start_handler import start
from handlers.platform_handler import choose_platform
from handlers.link_handler import receive_link
from handlers.format_handler import choose_format

BOT_TOKEN = os.getenv("8110654234:AAHawXh47X84oomkTli46StSgWtDUBSmF1w")

# States
CHOOSING_PLATFORM, GETTING_LINK, CHOOSING_FORMAT = range(3)


async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            CHOOSING_PLATFORM: [MessageHandler(filters.TEXT, choose_platform)],
            GETTING_LINK: [MessageHandler(filters.TEXT, receive_link)],
            CHOOSING_FORMAT: [MessageHandler(filters.TEXT, choose_format)],
        },
        fallbacks=[]
    )

    app.add_handler(conv_handler)

    print("Bot is running...")
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
