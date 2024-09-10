from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "5488825517:AAHMtH11kN9SGDY40Md4GhcHUMtXdwOgmaU"
CHANNELS = [
    {"id": "@Abduqodir_Yusufjonov", "name": "Kanal 1"},  # Vergul qo'shildi
    {"id": "@kiufmafia", "name": "Kanal 1"},  # Vergul qo'shildi
    {"id": "@uzdev2", "name": "Kanal 1"},  # Vergul qo'shildi
]


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())