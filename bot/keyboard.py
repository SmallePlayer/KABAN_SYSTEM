from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton
from aiogram import types
from Core.core import *

back_button = ReplyKeyboardBuilder()
back_button.add(types.KeyboardButton(text="База данных"))

def main_keyboard():
    main_printers = ReplyKeyboardBuilder()
    main_printers.add(KeyboardButton(text="Главное меню"))
    for i in range(0, get_printers_count()):
        main_printers.add(KeyboardButton(text=f"Принтер {i}"))
    main_printers.adjust(3, 3, 3)
    return main_printers

db_printers = ReplyKeyboardBuilder()
db_printers.add(types.KeyboardButton(text="Главное меню"))
db_printers.add(types.KeyboardButton(text="Новый принтер"))
db_printers.add(types.KeyboardButton(text="Все принтеры"))
db_printers.add(types.KeyboardButton(text="Удалить"))
db_printers.add(types.KeyboardButton(text="Обновить компонент"))
db_printers.adjust(3, 3, 3)

db_numlock_item = ReplyKeyboardBuilder()
db_numlock_item.add(types.KeyboardButton(text="Имя"))
db_numlock_item.add(types.KeyboardButton(text="Ip"))
db_numlock_item.add(types.KeyboardButton(text="Адрес камеры"))
db_numlock_item.add(types.KeyboardButton(text="Пин реле"))


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



