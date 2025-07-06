import logging
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from db.db import delete_printer, add_printer, update_printer
from bot.db_bot.fun_add_bot import print_all_printer
from bot.states import Navigation
import bot.keyboard as kb


db_bot = Router()

printer = {"id": None, "name": None, "ip": None, "camera": None}

class Form(StatesGroup):
    waiting_for_id = State()
    waiting_for_name = State()
    waiting_for_ip = State()
    waiting_for_camera = State()
    delete_for_printer = State()

    update_for_item = State()
    chooce_item = State()
    item_name = State()
    item_ip = State()
    item_camera = State()

@db_bot.message(F.text == "Обновить компонент")
async def update_item(message: types.Message, state: FSMContext):
    await state.set_state(Form.update_for_item)
    await message.answer("Напиши id принтера у которого хотите изменить что-то: ", 
            reply_markup=kb.back_button.as_markup(resize_keyboard=True))
    
@db_bot.message(Form.update_for_item)
async def write_id(message: types.Message, state: FSMContext):
    printer["id"] = message.text

    await state.set_state(Form.chooce_item)
    await message.answer("Выберите то что хотите поменять:", 
                reply_markup=kb.db_numlock_item.as_markup(resize_keyboard=True))

@db_bot.message(Form.chooce_item)
async def write_id(message: types.Message, state: FSMContext):
    item = message.text
    
    if item == "Имя":
        await state.set_state(Form.item_name)
    elif item == "Ip":
        await state.set_state(Form.item_ip)
    elif item == "Адрес камеры":
        await state.set_state(Form.item_camera)

    await message.answer("Введите то что хотите поменять: ", 
                reply_markup=types.ReplyKeyboardRemove())   

@db_bot.message(F.text == "Удалить")
async def delete(message: types.Message, state: FSMContext):
    await state.set_state(Form.delete_for_printer)
    await message.answer("Напиши id принтера который хотите удалить: ", 
            reply_markup=kb.back_button.as_markup(resize_keyboard=True))

@db_bot.message(F.text == "Все принтеры")
async def show_all_printers(message: types.Message):
    message_parts = print_all_printer()
    
    for part in message_parts:
        await message.answer(
            part,
            reply_markup=kb.db_printers.as_markup(resize_keyboard=True))
        
@db_bot.message(F.text == "Новый принтер")
async def req_id(message: types.Message, state: FSMContext):
    await state.set_state(Form.waiting_for_id)
    await message.answer("Введите id: ",
                reply_markup=kb.back_button.as_markup(resize_keyboard=True))
    
@db_bot.message(Form.item_name)
async def write_name(message: types.Message, state: FSMContext):
    printer["name"] = message.text
    update_printer(printer["id"], "name", printer["name"])
    await message.answer(f"поменяли name ", 
                reply_markup=kb.db_printers.as_markup(resize_keyboard=True))

@db_bot.message(Form.item_ip)
async def write_ip(message: types.Message, state: FSMContext):
    printer["ip"] = message.text
    update_printer(printer["id"], "ip", printer["ip"])
    await message.answer(f"поменяли ip ", 
                reply_markup=kb.db_printers.as_markup(resize_keyboard=True))
    
@db_bot.message(Form.item_camera)
async def write_camera(message: types.Message, state: FSMContext):
    printer["camera"] = message.text
    update_printer(printer["id"], "camera", printer["camera"])
    await message.answer(f"поменяли camera ", 
                reply_markup=kb.db_printers.as_markup(resize_keyboard=True))



@db_bot.message(Form.waiting_for_id)
async def write_id(message: types.Message, state: FSMContext):
    printer["id"] = message.text

    await state.set_state(Form.waiting_for_name)
    await message.answer("Введите имя принтера: ", 
                reply_markup=types.ReplyKeyboardRemove())
    
@db_bot.message(Form.waiting_for_name)
async def write_id(message: types.Message, state: FSMContext):
    printer["name"] = message.text

    await state.set_state(Form.waiting_for_ip)
    await message.answer("Введите ip принтера: ", 
                reply_markup=types.ReplyKeyboardRemove())
    
@db_bot.message(Form.waiting_for_ip)
async def write_id(message: types.Message, state: FSMContext):
    printer["ip"] = message.text

    await state.set_state(Form.waiting_for_camera)
    await message.answer("Введите camera принтера: ", 
                reply_markup=types.ReplyKeyboardRemove())
    
@db_bot.message(Form.waiting_for_camera)
async def write_id(message: types.Message, state: FSMContext):
    printer["camera"] = message.text
    
    add_printer(printer["id"], printer["name"], printer["ip"], printer["camera"])
 
    await state.clear()
    await message.answer("Данные сохранены", 
                reply_markup=kb.db_printers.as_markup(resize_keyboard=True))
    
@db_bot.message(Form.delete_for_printer)
async def delete(message: types.Message, state: FSMContext):
    printer_id = message.text
    if delete_printer(int(printer_id)):
        await state.clear()
        await message.answer(f"Удалили принтер под id {printer_id}", 
                reply_markup=kb.db_printers.as_markup(resize_keyboard=True))

    else:
        await message.answer(f"Не удалили принтер под id {printer_id}",
                reply_markup=kb.db_printers.as_markup(resize_keyboard=True))