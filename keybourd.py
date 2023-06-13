from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

klava = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Рассчитать калорийность продукта')
klava.add(button1)