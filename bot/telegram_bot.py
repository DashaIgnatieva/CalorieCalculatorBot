import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from add_address_for_search import add_address_in_sys_path; add_address_in_sys_path()
from config import bot_token

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Создаем экземпляр бота
bot = Bot(token=bot_token)

# Диспетчер
dp = Dispatcher(bot)

# Хендлер команды "start"
@dp.message_handler(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет!')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
