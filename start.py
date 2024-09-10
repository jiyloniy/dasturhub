# from aiogram import Bot, Dispatcher, Router, types
# from aiogram.filters import Command
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# import asyncio
# import logging
# from .utilits import check_channels
# from .bot import subscription_router
# logger = logging.getLogger(__name__)


# @subscription_router.message(Command("start"))
# async def cmd_start(message: types.Message):
    
#     await check_channels(message.from_user.id, message.chat.id)


# @subscription_router.callback_query(lambda c: c.data == "check_subscription")
# async def process_callback(callback_query: types.CallbackQuery):
#     await check_channels(callback_query.from_user.id, callback_query.message.chat.id)
#     await callback_query.answer()






async def check_subscription(user_id: int, channel_id: str):
    try:
        member = await bot.get_chat_member(channel_id, user_id)
        return member.status not in ["left", "kicked"]
    except Exception:
        return False

async def get_unsubscribed_channels(user_id: int):
    unsubscribed = []
    for channel in CHANNELS:
        if not await check_subscription(user_id, channel["id"]):
            unsubscribed.append(channel)
    return unsubscribed

def create_subscription_keyboard(channels):
    builder = InlineKeyboardBuilder()
    for channel in channels:
        builder.button(text=channel["name"], url=f"https://t.me/{channel['id'][1:]}", row_width=1)
    builder.button(text="✅ Tekshirish", callback_data="check_subscription")
    return builder.as_markup()

async def check_channels(user_id: int, chat_id: int):
    unsubscribed = await get_unsubscribed_channels(user_id)
    if not unsubscribed:
        await bot.send_message(chat_id, "Siz barcha kanallarga a'zo bo'lgansiz! Botdan foydalanishingiz mumkin.")
    else:
        keyboard = create_subscription_keyboard(unsubscribed)
        await bot.send_message(
            chat_id,
            "Botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling:",
            reply_markup=keyboard
        )

@subscription_router.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"User {message.from_user.id} started the bot")
    await check_channels(message.from_user.id, message.chat.id)

@subscription_router.callback_query(lambda c: c.data == "check_subscription")
async def process_callback(callback_query: types.CallbackQuery):
    await check_channels(callback_query.from_user.id, callback_query.message.chat.id)
    await callback_query.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Bot started")
    logger.info("Bot started")
    asyncio.run(main())