# bot/main.py
import os
from telegram.ext import Application, CommandHandler
from . import handlers # Import the handlers module

# Get the token from the environment variable set in Render
TOKEN = os.environ.get("TOKEN")

def main():
    """Sets up and runs the Telegram bot."""
    if not TOKEN:
        print("CRITICAL ERROR: The 'TOKEN' environment variable is not set.")
        return

    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", handlers.start))
    app.add_handler(CommandHandler("menu", handlers.menu))

    print("Bot is running... Press Ctrl-C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
