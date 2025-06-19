from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import  FSInputFile
from aiogram import F
from Core.config import BOT_TOKEN
from Core.core import *
import bot.keyboard as kb
from states import Navigation
from aiogram.fsm.context import FSMContext


logger = logging.getLogger('Bot')
setup_logger()

main_bot = Router()

state = False 

@main_bot.message(F.text.startswith("Принтер"))
async def status_printr_1(message: types.Message):
    id = message.text.split()[1]

    photo_name = create_photo(int(id))
    frame = FSInputFile(photo_name)

    #data = get_data(printer_id)
    #status = get_stat_print(id)
    name_printer = get_printer(id)

    logger.info(f"message bot ____ | frame {photo_name}")
    await message.answer_photo(frame)
    await message.answer(f"Фото с {name_printer[1]}", 
        reply_markup=kb.simple_printer_keyboard(id).as_markup(resize_keyboard=True))

@main_bot.message(F.text.startswith("Вкл/Выкл"))
async def status_printr_change(message: types.Message):
    id = message.text.split()[1]

    global state
    state = not state
    responce = edit_state_rele(state, id)

    await message.answer(f"Статус принтера {id}: {responce} \nОтвет реле: {responce}")