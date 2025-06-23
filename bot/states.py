from aiogram.fsm.state import StatesGroup, State

class Navigation(StatesGroup):
    MAIN_MENU = State()
    PRINTERS_MENU = State()
    DB_MENU = State()