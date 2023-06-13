import logging
from bot import dispatcher, bot
from aiogram.dispatcher.filters import Command, Text
from commands import *
import asyncio

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Команды
dispatcher.register_message_handler(start, Command('start'))
dispatcher.register_message_handler(help, Command('help'))
dispatcher.register_message_handler(count_cal ,Text(equals='Рассчитать калорийность продукта')) # Для вызова функции нужен текст с кнопки, полное совпадение

async def main():
    await dispatcher.start_polling(bot)

asyncio.run(main())