from bot import bot
from aiogram import types
from keybourd import klava

# Комманда /start
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Приветствую тебя в Калькуляторе Калорий!\nЕсли тебе нужна инструкция по командам бота, напиши /help',
                           reply_markup=klava)
    await message.delete()

# Комманда /help
async def help(message: types.Message):
    await message.answer('Описание возможностей бота')
    await message.delete()

async def count_cal(message: types.Message):
    await message.answer('Тут будет переход на инлайн клаву')
    await message.delete()
