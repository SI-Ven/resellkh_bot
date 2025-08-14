# bot/main.py

from telegram.ext import Application, CommandHandler
from .config import TOKEN
from .handlers import start, menu

def main():
    """Sets up and runs the Telegram bot."""
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))

    print("Bot is running... Press Ctrl-C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()