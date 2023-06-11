from aiogram import Bot, Dispatcher
from config import bot_token

# Создаем экземпляр бота
bot1 = Bot(token=bot_token)

# Диспетчер
dp = Dispatcher(bot1)