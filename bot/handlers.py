# bot/handlers.py
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Get URLs from environment variables set in Render.
# The second argument is a default value in case the variable isn't set.
LOGIN_URL = os.environ.get("LOGIN_URL", "https://www.resellkh.shop/login")
REGISTER_URL = os.environ.get("REGISTER_URL", "https://www.resellkh.shop/register")
TIKTOK_URL = os.environ.get("TIKTOK_URL", "https://www.tiktok.com/@resellkh")
FACEBOOK_URL = os.environ.get("FACEBOOK_URL", "https://web.facebook.com/profile.php?id=61578886787081")
PAGE_URL = os.environ.get("PAGE_URL", "https://web.facebook.com/profile.php?id=61578988574380")
CHANNEL_URL = os.environ.get("CHANNEL_URL", "https://t.me/resell_second_hand")
WEBSITE_URL = os.environ.get("WEBSITE_URL", "https://www.resellkh.shop")


def get_main_menu_keyboard():
    """Returns the keyboard with links from environment variables."""
    keyboard = [
        [InlineKeyboardButton("🛍️ Visit Our Shop", url=WEBSITE_URL)],
        [
            InlineKeyboardButton("✅ Register", url=REGISTER_URL),
            InlineKeyboardButton("🔑 Login", url=LOGIN_URL)
        ],
        [
            InlineKeyboardButton("🎵 TikTok", url=TIKTOK_URL),
            InlineKeyboardButton("📘 Facebook", url=FACEBOOK_URL)
        ],
        [
            InlineKeyboardButton("📰 Facebook Page", url=PAGE_URL),
            InlineKeyboardButton("📢 Channel", url=CHANNEL_URL)
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
