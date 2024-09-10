from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import asyncio
import logging
from handlers import start
logger = logging.getLogger(__name__)
BOT_TOKEN = "5488825517:AAHMtH11kN9SGDY40Md4GhcHUMtXdwOgmaU"
CHANNELS = [
    {"id": "@Abduqodir_Yusufjonov", "name": "Kanal 1"}
    
]


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(start.start_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot started")
    logger.info("Bot started")
    asyncio.run(main())