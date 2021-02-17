"""A template of telegram bot in Python."""
import sys
import logging
from decouple import config
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)


TOKEN = config("TOKEN")
"""Bot token obtained from @BotFather on Telegram."""
APP_URL = config("APP_URL", None)
"""App url on deployment server like https://app-name.herokuapp.com/."""
PORT = config("PORT", 5000)
"""PORT assigned by hosting server."""

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def start(update, context):
    """/start command handler."""
    context.bot.send_message(
        update.message.chat_id,
        "Hello!!, This a template of python telegram bot",  # Replace this to own text.
    )


def ping_pong(update, context):
    """ping message handler."""
    if update.message.text.lower() == "ping":
        context.bot.send_message(update.message.chat_id, "Ponggg!!!!")
    elif update.message.text.lower() == "pong":
        context.bot.send_message(update.message.chat_id, "Pingg!!!")


def main():
    """main function."""
    print("Starting Bot")
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler("start", start)
    ping_pong_handler = MessageHandler(Filters.text & (~Filters.command), ping_pong)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_pong_handler)
    if len(sys.argv) > 1 and sys.argv[1] == "-l":
        print("Starting updater.")
        updater.start_polling()
    else:
        updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN)
        print("Starting webhook.")
        updater.bot.setWebhook(APP_URL + TOKEN)
    print("Bot has been started.")
    updater.idle()


if __name__ == "__main__":
    main()
