# bot/main.py

from telegram.ext import Application, CommandHandler
from .config import TOKEN
from .handlers import start, help_command

def main():
    app = Application.builder().token(TOKEN).build()

    # Add commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()
