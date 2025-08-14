# bot/handlers.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from .config import WEBSITE_URL

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Open My Website 🌐", url=WEBSITE_URL)],
        [InlineKeyboardButton("Open in Browser 🌍", url=WEBSITE_URL + "?open=external")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello! 👋 Click a button below:",
        reply_markup=reply_markup
    )

# Example of future expansion command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "This bot can open my website.\n"
        "Commands:\n"
        "/start - Show the main menu\n"
        "/help - Show this help message"
    )
