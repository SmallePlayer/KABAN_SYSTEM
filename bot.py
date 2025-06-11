from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton
from aiogram import F
from config import BOT_TOKEN
from core import *



bot = Bot(token =BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    builder = ReplyKeyboardBuilder()

    for i in range(0, get_len_data()):
        builder.add(KeyboardButton(text=f"Принтер {i}"))

    
    await message.answer("Trun button", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text.startswith("Принтер"))
async def status_printr_1(message: types.Message):
    printer_id = message.text.split()[1]

    create_photo(int(printer_id))
    frame = FSInputFile(photo_path)
    #data = get_data(printer_id)
    status = get_stat_print(printer_id)

    await message.answer_photo(frame)
    await message.answer(status)



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())