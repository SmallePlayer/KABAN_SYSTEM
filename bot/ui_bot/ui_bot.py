from aiogram import types, Router
from aiogram.filters import Command
from aiogram import F
import bot.keyboard as kb
from states import Navigation
from aiogram.fsm.context import FSMContext


ui_bot = Router()

@ui_bot.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Navigation.MAIN_MENU)
    await message.answer("Выберете меню", 
        reply_markup=kb.main_ui_keyboard.as_markup(resize_keyboard=True))
    
@ui_bot.message((F.text == "Управление принтерами") | (F.text == "Принтеры"))
async def to_printers_menu(message: types.Message, state: FSMContext):
    await state.set_state(Navigation.PRINTERS_MENU)
    await message.answer("Выберите принтер", 
        reply_markup=kb.main_keyboard().as_markup(resize_keyboard=True))
    
@ui_bot.message(F.text == "Добавление принтера в базу данных")
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Navigation.DB_MENU)
    await message.answer(
        "Выберите действие:",
        reply_markup=kb.db_printers.as_markup(resize_keyboard=True))

@ui_bot.message(F.text == "Назад")
async def back_to_main(message: types.Message, state: FSMContext):
    await state.set_state(Navigation.MAIN_MENU)
    await message.answer("Главное меню", 
        reply_markup=kb.main_ui_keyboard.as_markup(resize_keyboard=True))