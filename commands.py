from bot import dp, bot1
from aiogram.dispatcher.filters import Command
from aiogram import types

# Хендлер команды "start"
@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет!Для того, что бы узнать о возможностях этого бота напиши команду /help')

# Хендлер команды "help"
@dp.message_handler(Command('help'))
async def help(message: types.Message):
    await message.answer('Описание возможностей бота')

# Функция для импорта хендлеров
def commands_file_handlers():
    dp.register_message_handler(start, Command('start'))
    dp.register_message_handler(help, Command('help'))