import logging
from bot import dp, bot1
from commands import commands_file_handlers
import asyncio

# Включаем логирование
logging.basicConfig(level=logging.INFO)

commands_file_handlers()

async def main():
    await dp.start_polling(bot1)

if __name__ == "__main__":
    asyncio.run(main())

