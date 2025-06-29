from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import  FSInputFile
from aiogram import F
from Core.config import BOT_TOKEN
from Core.core import *
import bot.keyboard as kb
from bot.states import Navigation
from aiogram.fsm.context import FSMContext


main_bot = Router()

state = False 

@main_bot.message(F.text.startswith("Принтер"))
async def status_printr_1(message: types.Message):
    name = message.text.split()[1]

    photo_name = create_photo(name)
    frame = FSInputFile(photo_name)

    #data = get_data(printer_id)
    #status = get_stat_print(id)

    await message.answer_photo(frame)
    await message.answer(f"Фото с {name}", 
        reply_markup=kb.simple_printer_keyboard(name).as_markup(resize_keyboard=True))

@main_bot.message(F.text.startswith("Аварийная остановка"))
async def status_printr_change(message: types.Message):
    id = message.text.split()[1]

    name = emeg_stop(id)


    await message.answer(f"Принтер {name} выполнил аварийную остановку")