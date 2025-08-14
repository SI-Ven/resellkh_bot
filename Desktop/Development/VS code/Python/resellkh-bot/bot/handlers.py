# bot/handlers.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# IMPORTANT: You must have LOGIN_URL and REGISTER_URL defined in your config.py
from .config import WEBSITE_URL, LOGIN_URL, REGISTER_URL

def get_main_menu_keyboard():
    """Returns the keyboard with links to your website."""
    keyboard = [
        [InlineKeyboardButton("🛍️ Visit Our Shop", url=WEBSITE_URL)],
        [
            InlineKeyboardButton("✅ Register", url=REGISTER_URL),
            InlineKeyboardButton("🔑 Login", url=LOGIN_URL)
        ],
        [
            InlineKeyboardButton("🎵 TikTok", url="https://www.tiktok.com/@resellkh"),
            InlineKeyboardButton("📘 Facebook", url="https://web.facebook.com/profile.php?id=61578886787081")
        ],
        [
            InlineKeyboardButton("📰 Facebook Page", url="https://web.facebook.com/profile.php?id=61578988574380"),
            InlineKeyboardButton("📢 Channel", url="https://t.me/resell_second_hand")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message with a link to the main menu."""
    await update.message.reply_text(
        "Welcome to ResellKH! Please visit our website to register or log in.",
        reply_markup=get_main_menu_keyboard()
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Displays the main inline menu."""
    await update.message.reply_text(
        text="👋 Here are our official links:",
        reply_markup=get_main_menu_keyboard()
    )
