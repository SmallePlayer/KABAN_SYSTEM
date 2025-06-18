from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton
from aiogram import types
from Core.core import *


def main_keyboard():
    main_printers = ReplyKeyboardBuilder()
    main_printers.add(KeyboardButton(text="Назад"))
    for i in range(0, get_printers_count()):
        main_printers.add(KeyboardButton(text=f"Принтер {i}"))
    main_printers.adjust(3, 3, 3)
    return main_printers

db_printers = ReplyKeyboardBuilder()
db_printers.adjust(3, 3, 3)
db_printers.add(types.KeyboardButton(text="Назад"))
db_printers.add(types.KeyboardButton(text="Ввести printer"))
db_printers.add(types.KeyboardButton(text="Показать all printers"))
db_printers.add(types.KeyboardButton(text="Delete printer"))
db_printers.add(types.KeyboardButton(text="Update printer item"))

db_numlock_item = ReplyKeyboardBuilder()
db_numlock_item.add(types.KeyboardButton(text="1"))
db_numlock_item.add(types.KeyboardButton(text="2"))
db_numlock_item.add(types.KeyboardButton(text="3"))
db_numlock_item.add(types.KeyboardButton(text="4"))


def simple_printer_keyboard(id):
    simple_printer = ReplyKeyboardBuilder()
    simple_printer.row(
        types.KeyboardButton(text="Принтеры"),
        types.KeyboardButton(text=f"Вкл/Выкл {id}")
    )
    simple_printer.row(
        types.KeyboardButton(text=f"Принтер {id}")
    )

    return simple_printer


main_ui_keyboard = ReplyKeyboardBuilder()
main_ui_keyboard.row(types.KeyboardButton(text="Управление принтерами"))
main_ui_keyboard.row(types.KeyboardButton(text=f"Добавление принтера в базу данных"))



