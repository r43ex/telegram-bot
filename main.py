import os
import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# تنظیم لاگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# توکن ربات از محیط Replit
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("لطفاً TELEGRAM_BOT_TOKEN رو از Secrets تنظیم کنید!")

# ================== متن‌ها و قیمت‌ها ==================
texts = {
    "menu": "به فروشگاه پریمیوم خوش اومدی!\n\nیکی از گزینه‌های زیر رو انتخاب کن:",
    "stars": (
        "<b>استارز تلگرام</b>\n\n"
        "<code>1 Star = 2,050T</code>\n\n"
        "50⭐ — 102,500T\n"
        "100⭐ — 205,000T\n"
        "200⭐ — 410,000