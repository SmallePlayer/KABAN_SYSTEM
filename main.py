from aiogram import Bot, Dispatcher
from Core.core import *
from bot.main_bot.bot import main_bot
from bot.ui_bot.ui_bot import ui_bot
from bot.db_bot.db_bot_meneger import db_bot
import asyncio

dp = Dispatcher()

dp.include_router(ui_bot)
dp.include_router(main_bot)
dp.include_router(db_bot)


bot = Bot(token=BOT_TOKEN)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())