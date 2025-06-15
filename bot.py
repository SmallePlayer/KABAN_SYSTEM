from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton
from aiogram import F
from config import BOT_TOKEN
from core import *

logger = logging.getLogger('Bot')

bot = Bot(token =BOT_TOKEN)
dp = Dispatcher()

state = False

@dp.message(Command("start", "=", prefix="</"))
async def start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    logger.info("Command start")

    for i in range(0, get_printers_count()):
        builder.add(KeyboardButton(text=f"Принтер {i}"))

    builder.adjust(3, 3, 3)

    await message.answer("Выберете принтер", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text.startswith("Принтер"))
async def status_printr_1(message: types.Message):
    id = message.text.split()[1]

    photo_name = create_photo(int(id))
    frame = FSInputFile(photo_name)

    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="<="),
        types.KeyboardButton(text=f"Вкл/Выкл {id}")
    )
    builder.row(
        types.KeyboardButton(text=f"Принтер {id}")
    )

    #data = get_data(printer_id)
    #status = get_stat_print(id)

    logger.info(f"message bot ____ | frame {photo_name}")
    await message.answer_photo(frame)
    await message.answer("фото", reply_markup=builder.as_markup(resize_keyboard=True))

@dp.message(F.text.startswith("Вкл/Выкл"))
async def status_printr_change(message: types.Message):
    id = message.text.split()[1]

    global state
    state = not state
    responce = edit_state_rele(state, id)

    await message.answer(f"Статус принтера {id}: {responce} \nОтвет реле: {responce}")

@dp.message(Command("hello"))
async def cmd_hello(message: Message):
    chat_id = message.chat.id
    name = message.from_user.full_name
    print(f"{name} = {chat_id}")
    await message.answer(
        f"Привет, {name}"
    )



async def main():
    await dp.start_polling(bot)
    logger.debug("start bot")

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())